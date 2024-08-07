"""
from pydantic import BaseModel
from typing import Optional

class OrderMenuItemBase(BaseModel):
    order_tracking_num: Optional[int]
    menu_item_id: Optional[int]

class OrderMenuItemCreate(OrderMenuItemBase):
    pass

class OrderMenuItemUpdate(OrderMenuItemBase):
    pass

class OrderMenuItem(OrderMenuItemBase):
    # IDK if the following is necessary, maybe already handled by inherited foreign key values
    # order: Order
    # menu_item: MenuItem
    class ConfigDict:
        from_attributes = True
"""