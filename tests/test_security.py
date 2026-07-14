from security import hash_password, verify_password


def test_hash_password_returns_different_string_than_input():
    raw = "supersecret123"
    hashed = hash_password(raw)
    assert hashed != raw


def test_verify_password_correct():
    raw = "supersecret123"
    hashed = hash_password(raw)
    assert verify_password(raw, hashed) is True


def test_verify_password_incorrect():
    hashed = hash_password("supersecret123")
    assert verify_password("wrongpassword", hashed) is False


def test_hash_password_is_salted():
    raw = "supersecret123"
    hash1 = hash_password(raw)
    hash2 = hash_password(raw)
    assert hash1 != hash2
