from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from decimal import Decimal


class PromotionBase(BaseModel):
    code: Optional[str] = Field(None, max_length=50)
    discount_amt: Optional[Decimal]
    expiration_date: Optional[datetime]


class PromotionCreate(PromotionBase):
    code: str
    discount_amt: Decimal
    expiration_date: datetime


class PromotionUpdate(PromotionBase):
    pass


class CustomerPaymentPromotion(BaseModel):
    customer_id: int
    payment_id: int
    promotion_id: int

    class Config:
        orm_mode = True


class Promotion(PromotionBase):
    id: int
    code: str
    discount_amt: Decimal
    expiration_date: datetime
    customers_payments_promotions: List[CustomerPaymentPromotion] = []

    class Config:
        orm_mode = True
