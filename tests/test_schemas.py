import pytest
from pydantic import ValidationError
from schemas import UserCreate


def test_user_create_valid():
    user = UserCreate(username="moe", email="moe@example.com", password="pass123")
    assert user.username == "moe"
    assert user.email == "moe@example.com"


def test_user_create_invalid_email_raises():
    with pytest.raises(ValidationError):
        UserCreate(username="moe", email="not-an-email", password="pass123")


def test_user_create_missing_field_raises():
    with pytest.raises(ValidationError):
        UserCreate(username="moe", email="moe@example.com")
