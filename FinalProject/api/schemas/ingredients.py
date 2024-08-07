"""
from pydantic import BaseModel, Field
from typing import Optional, List


class IngredientBase(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    amount: Optional[int]
    amount_unit: Optional[str] = Field(None, max_length=20)


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[int] = None
    amount_unit: Optional[str] = None


class Ingredient(IngredientBase):
    id: int
    class ConfigDict:
        from_attributes = True
"""