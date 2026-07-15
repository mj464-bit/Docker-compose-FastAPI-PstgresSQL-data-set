import pytest
from pydantic import ValidationError
from schemas import CalculationCreate
from models import OperationType


def test_calculation_create_valid():
    calc = CalculationCreate(a=10, b=2, type=OperationType.DIVIDE)
    assert calc.a == 10
    assert calc.b == 2
    assert calc.type == OperationType.DIVIDE


def test_calculation_create_divide_by_zero_raises():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=0, type=OperationType.DIVIDE)


def test_calculation_create_invalid_type_raises():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=2, type="NotAnOperation")


def test_calculation_create_add_allows_zero_b():
    # zero is only disallowed for Divide, should be fine for Add
    calc = CalculationCreate(a=10, b=0, type=OperationType.ADD)
    assert calc.b == 0
