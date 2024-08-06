from pydantic import BaseModel
from typing import Optional

class PaymentBase(BaseModel):
    amount: float
    payment_method: str
    transaction_status: str

class PaymentCreate(PaymentBase):
    order_id: int

class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    payment_method: Optional[str] = None
    transaction_status: Optional[str] = None

class Payment(PaymentBase):
    id: int
    order_id: int

    class Config:
        orm_mode = True
