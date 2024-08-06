from pydantic import BaseModel
from typing import Optional

class OrderMenuItemBase(BaseModel):
    order_tracking_num: Optional[int]
    menu_item_id: Optional[int]

class OrderMenuItemCreate(OrderMenuItemBase):
    order_tracking_num: int
    menu_item_id: int

class OrderMenuItemUpdate(OrderMenuItemBase):
    pass

class OrderMenuItem(OrderMenuItemBase):
    order_tracking_num: int
    menu_item_id: int

    class Config:
        orm_mode = True
