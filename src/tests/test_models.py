import pytest
from src.models import db, User, Order

@pytest.fixture
def init_db():
    """Ініціалізація бази даних перед тестами"""
    db.create_all()
    yield db
    db.drop_all()

def test_user_model(init_db):
    """Тест для моделі користувача"""
    user = User(username="test_user", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    # Перевірка, чи користувач зберігається в базі
    saved_user = User.query.get(user.id)
    assert saved_user is not None
    assert saved_user.username == "test_user"
    assert saved_user.email == "test@example.com"

def test_order_model(init_db):
    """Тест для моделі замовлення"""
    order = Order(customer_id=1, product_id=101, quantity=2, status="pending")
    db.session.add(order)
    db.session.commit()

    # Перевірка, чи замовлення зберігається в базі
    saved_order = Order.query.get(order.id)
    assert saved_order is not None
    assert saved_order.customer_id == 1
    assert saved_order.product_id == 101
    assert saved_order.quantity == 2
    assert saved_order.status == "pending"

def test_order_relation(init_db):
    """Тест для перевірки зв'язку між користувачем та замовленням"""
    user = User(username="test_user", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    order = Order(customer_id=user.id, product_id=101, quantity=2, status="pending")
    db.session.add(order)
    db.session.commit()

    # Перевірка, чи замовлення пов'язано з користувачем
    saved_order = Order.query.get(order.id)
    assert saved_order.customer_id == user.id
    assert saved_order.customer.username == "test_user"

def test_user_unique_email(init_db):
    """Тест для перевірки унікальності email користувача"""
    user1 = User(username="user1", email="unique@example.com")
    db.session.add(user1)
    db.session.commit()

    user2 = User(username="user2", email="unique@example.com")
    
    with pytest.raises(Exception):  # Очікуємо виняток через порушення унікальності
        db.session.add(user2)
        db.session.commit()
