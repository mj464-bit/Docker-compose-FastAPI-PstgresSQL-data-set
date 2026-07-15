import pytest
from sqlalchemy.exc import DataError

from models import Calculation, OperationType
from calculation_factory import CalculationFactory


def test_create_calculation_success(db_session):
    result = CalculationFactory.compute(OperationType.ADD, 4, 3)
    calc = Calculation(a=4, b=3, type=OperationType.ADD, result=result)
    db_session.add(calc)
    db_session.commit()

    saved = db_session.query(Calculation).filter_by(id=calc.id).first()
    assert saved is not None
    assert saved.a == 4
    assert saved.b == 3
    assert saved.type == OperationType.ADD
    assert saved.result == 7
    assert saved.created_at is not None


def test_create_calculation_with_user(db_session):
    from models import User
    from security import hash_password

    user = User(username="calcowner", email="calcowner@example.com",
                password_hash=hash_password("pass123"))
    db_session.add(user)
    db_session.commit()

    calc = Calculation(a=10, b=2, type=OperationType.DIVIDE, result=5.0,
                       user_id=user.id)
    db_session.add(calc)
    db_session.commit()

    saved = db_session.query(Calculation).filter_by(id=calc.id).first()
    assert saved.user_id == user.id
    assert saved.user.username == "calcowner"


def test_invalid_type_rejected_at_db_level(db_session):
    # bypass Pydantic entirely and try to force a bad enum value straight
    # through SQLAlchemy/Postgres, to prove the DB-level enum constraint works
    with pytest.raises(Exception):
        db_session.execute(
            "INSERT INTO app_calculations (a, b, type) VALUES (1, 2, 'NotAnOperation')"
        )
        db_session.commit()
