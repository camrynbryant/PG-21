from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
   __tablename__ = "payments"

   id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   transaction_status = Column(String(50))

   customers_payments_promotions = relationship("CustomerPaymentPromotion", back_populates = "payments")
