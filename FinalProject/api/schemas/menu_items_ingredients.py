"""
from pydantic import BaseModel
from typing import Optional


class MenuItemIngredientBase(BaseModel):
    amount: Optional[int]


class MenuItemIngredientCreate(MenuItemIngredientBase):
    menu_item_id: int
    ingredient_id: int


class MenuItemIngredientUpdate(BaseModel):
    menu_item_id: int
    ingredient_id: int


class MenuItemIngredient(MenuItemIngredientBase):
    menu_item_id: int
    ingredient_id: int

    # IDK if the following is necessary, maybe already handled by foreign key values
    # menu_item: MenuItem
    # ingredient: Ingredient
    class ConfigDict:
        from_attributes = True
"""