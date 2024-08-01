"""
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class CustomerPaymentPromotion:
   __tablename__ = "customers_payments_promotions"


   customer_id = (Integer, ForeignKey("customers.id"))
   payment_id = (Integer, ForeignKey("payments.id"))
   promotion_id = (Integer, ForeignKey("promotions.id"))

   __table_args__ = (
       PrimaryKeyConstraint("customer_id", "payment_id", "promotion_id"),
       {},
   )

   customers = relationship("Customer", back_populates = "customers_payments_promotions")
   payments = relationship("Payment", back_populates = "customers_payments_promotions")
   promotions = relationship("Promotion", back_populates = "customers_payments_promotions")
"""

