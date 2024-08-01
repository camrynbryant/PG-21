"""
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotion:
   __tablename__ = "promotions"


   id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   code = Column(String(50))
   discount_amt = Column(Double(2))
   expiration_date = Column(DATETIME, nullable=False)


   customers_payments_promotions = relationship("CustomerPaymentPromotion", back_populates = "promotions")
"""