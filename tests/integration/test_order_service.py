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

def test_create_order(client, init_db):
    """Тест для інтеграції створення замовлення через API"""
    user = User(username="test_user", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    response = client.post('/create_order', json={
        'customer_id': user.id,
        'product_id': 101,
        'quantity': 2
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'order_id' in data
    assert data['status'] == 'pending'

def test_get_order(client, init_db):
    """Тест для інтеграції отримання замовлення через API"""
    user = User(username="test_user", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    order = Order(customer_id=user.id, product_id=101, quantity=2, status='pending')
    db.session.add(order)
    db.session.commit()

    response = client.get(f'/get_order/{order.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'pending'
