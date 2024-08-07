from decimal import Decimal

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(200))
    price = Column(Float)
    calories = Column(Integer)
    food_category = Column(String(50))

    orders_menu_items = relationship("OrderMenuItem", back_populates="menu_items")
    menu_items_ingredients = relationship("MenuItemIngredient", back_populates = "menu_items")
