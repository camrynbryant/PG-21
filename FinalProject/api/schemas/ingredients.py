from pydantic import BaseModel, Field
from typing import Optional, List

class IngredientBase(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    amount: Optional[int]
    amount_unit: Optional[str] = Field(None, max_length=20)


class IngredientCreate(IngredientBase):
    name: str
    amount: int
    amount_unit: str


class IngredientUpdate(IngredientBase):
    pass


class MenuItemIngredient(BaseModel):
    id: int
    menu_item_id: int
    ingredient_id: int

    class Config:
        orm_mode = True


class Ingredient(IngredientBase):
    id: int
    menu_items_ingredients: List[MenuItemIngredient] = []

    class Config:
        orm_mode = True
