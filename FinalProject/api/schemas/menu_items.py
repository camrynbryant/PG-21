from pydantic import BaseModel, Field
from typing import Optional, List
from decimal import Decimal


class MenuItemBase(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = Field(None, max_length=200)
    price: Optional[Decimal]
    calories: Optional[int]
    food_category: Optional[str] = Field(None, max_length=50)


class MenuItemCreate(MenuItemBase):
    name: str
    description: str
    price: Decimal
    calories: int
    food_category: str


class MenuItemUpdate(MenuItemBase):
    pass


class OrderMenuItem(BaseModel):
    id: int
    order_id: int
    menu_item_id: int

    class Config:
        orm_mode = True


class MenuItemIngredient(BaseModel):
    id: int
    menu_item_id: int
    ingredient_id: int

    class Config:
        orm_mode = True

class MenuItem(MenuItemBase):
    id: int
    orders_menu_items: List[OrderMenuItem] = []
    menu_items_ingredients: List[MenuItemIngredient] = []

    class Config:
        orm_mode = True
