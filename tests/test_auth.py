from app.auth import create_user, authenticate_user
from app.models import fake_db

def test_valid_login():
    fake_db.clear()
    create_user("alice", "password123")
    assert authenticate_user("alice", "password123") is True

def test_wrong_password_login():
    fake_db.clear()
    create_user("bob", "secret")
    assert authenticate_user("bob", "wrongpass") is False  # ❌ Change to False to fix
