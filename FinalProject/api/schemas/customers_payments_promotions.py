from pydantic import BaseModel
from typing import Optional


class CustomerPaymentPromotionBase(BaseModel):
    customer_id: Optional[int] = None
    payment_id: Optional[int] = None
    promotion_id: Optional[int] = None


class CustomerPaymentPromotionCreate(CustomerPaymentPromotionBase):
    pass


class CustomerPaymentPromotionUpdate(BaseModel):
    customer_id: int
    payment_id: int
    promotion_id: int


class CustomerPaymentPromotion(CustomerPaymentPromotionBase):
    #IDK if the following is necessary, maybe already handled by inherited foreign key values
    #customer: Customer
    #payment: Payment
    #promotion: Promotion

    class ConfigDict:
        from_attributes = True
