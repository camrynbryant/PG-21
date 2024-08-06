from pydantic import BaseModel, Field
from typing import Optional, List


class PaymentBase(BaseModel):
    transaction_status: Optional[str] = Field(None, max_length=50)


class PaymentCreate(PaymentBase):
    transaction_status: str


class PaymentUpdate(PaymentBase):
    pass


class CustomerPaymentPromotion(BaseModel):
    id: int
    customer_id: int
    payment_id: int
    promotion_id: int

    class Config:
        orm_mode = True


class Payment(PaymentBase):
    id: int
    customers_payments_promotions: List[CustomerPaymentPromotion] = []

    class Config:
        orm_mode = True
