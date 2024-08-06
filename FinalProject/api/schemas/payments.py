from pydantic import BaseModel, Field
from typing import Optional, List


class PaymentBase(BaseModel):
    transaction_status: Optional[str] = Field(None, max_length=50)


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    transaction_status: Optional[str] = None

class Payment(PaymentBase):
    id: int
    class ConfigDict:
        from_attributes = True
