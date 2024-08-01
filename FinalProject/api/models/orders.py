"""
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
   __tablename__ = "orders"


   tracking_num = Column(Integer, primary_key=True, index=True, autoincrement=True)
   status = Column(String(50))
   date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
   price = Column(Double(2))
   details_link = Column(String(200))
   customer_id = Column(Integer, ForeignKey("customers.id"))


   customers = relationship("Customer", back_populates="orders")
   orders_menu_items = relationship("OrderMenuItem", back_populates="orders")
"""