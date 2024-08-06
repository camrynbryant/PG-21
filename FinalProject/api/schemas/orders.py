from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from decimal import Decimal


class OrderBase(BaseModel):
    status: Optional[str] = Field(None, max_length=50)
    date: Optional[datetime] = Field(default_factory=datetime.now)
    price: Optional[Decimal]
    details_link: Optional[str] = Field(None, max_length=200)


class OrderCreate(OrderBase):
    customer_id: int


class OrderUpdate(OrderBase):
    pass


class OrderMenuItem(BaseModel):
    id: int
    order_id: int
    menu_item_id: int

    class Config:
        orm_mode = True


class Order(OrderBase):
    tracking_num: int
    customer_id: int
    orders_menu_items: List[OrderMenuItem] = []

    class Config:
        orm_mode = True
