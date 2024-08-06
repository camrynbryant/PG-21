from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DECIMAL

from FinalProject.api.models.customers import Customer


class OrderBase(BaseModel):
    status: Optional[str] = Field(None, max_length=50)
    price: Optional[Decimal]
    details_link: Optional[str] = Field(None, max_length=200)


class OrderCreate(OrderBase):
    customer_id: int


class OrderUpdate(BaseModel):
    status: Optional[str] = None
    price: Optional[DECIMAL] = None
    details_link: Optional[str] = None
    customer_id: Optional[int] = None


class Order(OrderBase):
    tracking_num: int
    customer: Customer

    class ConfigDict:
        from_attributes = True
