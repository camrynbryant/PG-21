from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Customer(Base):
   __tablename__ = "customers"


   id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   name = Column(String(50))
   email = Column(String(50))
   phone_number = Column(String(20))
   address = Column(String(100))


   reviews = relationship("Review", back_populates="customers")
   orders = relationship("Order", back_populates="customers")
   customers_payments_promotions = relationship("CustomerPaymentPromotion", back_populates = "customers")
