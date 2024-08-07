from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class MenuItemIngredient(Base):
    __tablename__ = "menu_items_ingredients"

    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))
    amount = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("menu_item_id", "ingredient_id"),
        {},
    )

    menu_items = relationship("MenuItem", back_populates="menu_items_ingredients")
    ingredients = relationship("Ingredient", back_populates="menu_items_ingredients")
