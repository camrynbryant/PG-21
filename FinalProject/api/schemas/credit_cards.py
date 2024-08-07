"""
from pydantic import BaseModel, Field
from typing import Optional


class CreditCardBase(BaseModel):
    card_num: Optional[str] = Field(None, max_length=50)
    cvc: Optional[str] = Field(None, max_length=5)


class CreditCardCreate(CreditCardBase):
    payment_id: Optional[int] = None


class CreditCardUpdate(BaseModel):
    card_num: Optional[str] = Field(None, max_length=50)
    cvc: Optional[str] = Field(None, max_length=5)


class CreditCard(CreditCardBase):
    payment_id: int

    # IDK if the following is necessary, maybe already handled by  foreign key values
    # payment: Payment
    class Config:
        orm_mode = True
"""