
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
class Ingredient:
   __tablename__ = "ingredients"


   id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   name = Column(String(50))
   amount = Column(Double(2))
   amount_unit = Column(String(20))


   #menu_items_ingredients = relationship("MenuItemIngredient", back_populates="ingredients")
