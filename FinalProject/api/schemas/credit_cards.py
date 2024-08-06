from pydantic import BaseModel, Field
from typing import Optional


class CreditCardBase(BaseModel):
    card_num: Optional[str] = Field(None, max_length=50)
    cvc: Optional[str] = Field(None, max_length=5)


class CreditCardCreate(CreditCardBase):
    pass

class CreditCardUpdate(BaseModel):
    card_num: Optional[str] = Field(None, max_length=50)
    cvc: Optional[str] = Field(None, max_length=5)


class CreditCard(CreditCardBase):

    class Config:
        orm_mode = True
