
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DECIMAL, Double

from .customers import Customer


class OrderBase(BaseModel):
    status: str
    price: float
    details_link: str


class OrderCreate(OrderBase):
    customer_id: int


class OrderUpdate(BaseModel):
    status: Optional[str] = None
    price: Optional[float] = None
    details_link: Optional[str] = None
    customer_id: Optional[int] = None


class Order(OrderBase):
    tracking_num: int
    date: datetime
    customer: Customer = None

    class ConfigDict:
        from_attributes = True

