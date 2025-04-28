import pytest
from src.app import app
from src.models import db, Order

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_db():
    """Ініціалізація бази даних перед тестами"""
    db.create_all()
    yield db
    db.drop_all()

def test_create_order(client, init_db):
    """Тест для створення замовлення"""
    response = client.post('/create_order', json={
        'customer_id': 1,
        'product_id': 101,
        'quantity': 2
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'order_id' in data
    assert data['status'] == 'pending'

def test_get_order(client, init_db):
    """Тест для отримання замовлення"""
    order = Order(customer_id=1, product_id=101, quantity=2, status='pending')
    db.session.add(order)
    db.session.commit()

    response = client.get(f'/get_order/{order.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'pending'

def test_update_order_status(client, init_db):
    """Тест для оновлення статусу замовлення"""
    order = Order(customer_id=1, product_id=101, quantity=2, status='pending')
    db.session.add(order)
    db.session.commit()

    response = client.put(f'/update_order_status/{order.id}', json={
        'status': 'shipped'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'shipped'
