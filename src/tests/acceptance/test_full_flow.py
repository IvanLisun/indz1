import pytest
from src.app import app
from src.models import db, User, Order

@pytest.fixture
def client():
    """Фікстура для тестування API"""
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_db():
    """Ініціалізація бази даних перед тестами"""
    db.create_all()
    yield db
    db.drop_all()

def test_full_order_flow(client, init_db):
    """Приймальний тест для повного процесу створення замовлення"""
    # 1. Створюємо користувача
    response = client.post('/create_user', json={
        'username': 'test_user',
        'email': 'test@example.com'
    })
    assert response.status_code == 200
    user_data = response.get_json()
    user_id = user_data['user_id']

    # 2. Створюємо замовлення
    response = client.post('/create_order', json={
        'customer_id': user_id,
        'product_id': 101,
        'quantity': 2
    })
    assert response.status_code == 200
    order_data = response.get_json()
    order_id = order_data['order_id']
    assert order_data['status'] == 'pending'

    # 3. Оновлюємо статус замовлення
    response = client.put(f'/update_order_status/{order_id}', json={
        'status': 'shipped'
    })
    assert response.status_code == 200
    updated_order = response.get_json()
    assert updated_order['status'] == 'shipped'

    # 4. Перевіряємо, що замовлення успішно оновлене
    response = client.get(f'/get_order/{order_id}')
    assert response.status_code == 200
    final_order = response.get_json()
    assert final_order['status'] == 'shipped'
