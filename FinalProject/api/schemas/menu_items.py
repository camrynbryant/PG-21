"""
from pydantic import BaseModel, Field
from typing import Optional, List
from decimal import Decimal

from sqlalchemy import DECIMAL


class MenuItemBase(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = Field(None, max_length=200)
    price: Optional[float]
    calories: Optional[int]
    food_category: Optional[str] = Field(None, max_length=50)


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None


class MenuItem(MenuItemBase):
    id: int
    class ConfigDict:
        from_attributes = True
"""