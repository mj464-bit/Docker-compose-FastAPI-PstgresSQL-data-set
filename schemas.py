from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, model_validator
from models import OperationType


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CalculationCreate(BaseModel):
    a: float
    b: float
    type: OperationType
    user_id: Optional[int] = None

    @model_validator(mode="after")
    def no_divide_by_zero(self):
        if self.type == OperationType.DIVIDE and self.b == 0:
            raise ValueError("b cannot be zero when type is Divide")
        return self


class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: OperationType
    result: Optional[float]
    user_id: Optional[int]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
