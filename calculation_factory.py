from models import OperationType


class CalculationFactory:
    """Maps an OperationType to the function that performs it."""

    _operations = {
        OperationType.ADD: lambda a, b: a + b,
        OperationType.SUB: lambda a, b: a - b,
        OperationType.MULTIPLY: lambda a, b: a * b,
        OperationType.DIVIDE: lambda a, b: a / b,
    }

    @classmethod
    def compute(cls, operation: OperationType, a: float, b: float) -> float:
        if operation not in cls._operations:
            raise ValueError(f"Unsupported operation: {operation}")
        if operation == OperationType.DIVIDE and b == 0:
            raise ValueError("Cannot divide by zero")
        func = cls._operations[operation]
        return func(a, b)
