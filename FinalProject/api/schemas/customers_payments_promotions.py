from pydantic import BaseModel
from typing import Optional

class CustomerPaymentPromotionBase(BaseModel):
    customer_id: Optional[int]
    payment_id: Optional[int]
    promotion_id: Optional[int]

class CustomerPaymentPromotionCreate(CustomerPaymentPromotionBase):
    customer_id: int
    payment_id: int
    promotion_id: int

class CustomerPaymentPromotionUpdate(BaseModel):
    customer_id: Optional[int] = None
    payment_id: Optional[int] = None
    promotion_id: Optional[int] = None

class CustomerPaymentPromotion(CustomerPaymentPromotionBase):
    customer_id: int
    payment_id: int
    promotion_id: int

    class Config:
        orm_mode = True
