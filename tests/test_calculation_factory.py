import pytest
from calculation_factory import CalculationFactory
from models import OperationType


def test_add():
    assert CalculationFactory.compute(OperationType.ADD, 4, 3) == 7


def test_sub():
    assert CalculationFactory.compute(OperationType.SUB, 4, 3) == 1


def test_multiply():
    assert CalculationFactory.compute(OperationType.MULTIPLY, 4, 3) == 12


def test_divide():
    assert CalculationFactory.compute(OperationType.DIVIDE, 9, 3) == 3.0


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        CalculationFactory.compute(OperationType.DIVIDE, 9, 0)
