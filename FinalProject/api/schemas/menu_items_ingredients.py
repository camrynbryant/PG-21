from pydantic import BaseModel
from typing import Optional


class MenuItemIngredientBase(BaseModel):
    amount: Optional[int]


class MenuItemIngredientCreate(MenuItemIngredientBase):
    menu_item_id: int
    ingredient_id: int
    amount: int


class MenuItemIngredientUpdate(MenuItemIngredientBase):
    pass


class MenuItemIngredient(MenuItemIngredientBase):
    menu_item_id: int
    ingredient_id: int

    class Config:
        orm_mode = True
