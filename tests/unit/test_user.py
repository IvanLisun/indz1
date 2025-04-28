import pytest
from src.models import db, User

@pytest.fixture
def init_db():
    """Ініціалізація бази даних перед тестами"""
    db.create_all()
    yield db
    db.drop_all()

def test_user_creation(init_db):
    """Тест для створення користувача"""
    user = User(username="test_user", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    saved_user = User.query.get(user.id)
    assert saved_user is not None
    assert saved_user.username == "test_user"
    assert saved_user.email == "test@example.com"

def test_user_duplicate_email(init_db):
    """Тест для перевірки уникальності email"""
    user1 = User(username="user1", email="unique@example.com")
    db.session.add(user1)
    db.session.commit()

    user2 = User(username="user2", email="unique@example.com")
    
    with pytest.raises(Exception):
        db.session.add(user2)
        db.session.commit()
