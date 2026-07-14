import pytest
from sqlalchemy.exc import IntegrityError

from models import User
from security import hash_password


def test_create_user_success(db_session):
    user = User(
        username="moe",
        email="moe@example.com",
        password_hash=hash_password("pass123"),
    )
    db_session.add(user)
    db_session.commit()

    saved = db_session.query(User).filter_by(username="moe").first()
    assert saved is not None
    assert saved.email == "moe@example.com"
    assert saved.created_at is not None


def test_duplicate_username_raises(db_session):
    db_session.add(User(username="moe", email="a@example.com", password_hash="x"))
    db_session.commit()

    db_session.add(User(username="moe", email="b@example.com", password_hash="x"))
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_duplicate_email_raises(db_session):
    db_session.add(User(username="user1", email="dupe@example.com", password_hash="x"))
    db_session.commit()

    db_session.add(User(username="user2", email="dupe@example.com", password_hash="x"))
    with pytest.raises(IntegrityError):
        db_session.commit()
