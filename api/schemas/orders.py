from pydantic import BaseModel, Field, fields, computed_field, SerializeAsAny
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DECIMAL, Double



class OrderBase(BaseModel):
    status: str
    price: float
    details_link: str
    type: str


class OrderCreate(OrderBase):
    customer_id: int


class OrderUpdate(BaseModel):
    status: Optional[str] = None
    price: Optional[float] = None
    details_link: Optional[str] = None
    customer_id: Optional[int] = None
    type: Optional[str] = None


class Order(OrderBase):
    tracking_num: int
    date: datetime
    customer_id: int

    class ConfigDict:
        from_attributes = True

class OrderNum(BaseModel):
    num_orders: int


class NumOrder:
    pass