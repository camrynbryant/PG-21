from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class CustomerPaymentPromotion(Base):
    __tablename__ = "customers_payments_promotions"

    customer_id = Column(Integer, ForeignKey("customers.id"))
    payment_id = Column(Integer, ForeignKey("payments.id"))
    promotion_id = Column(Integer, ForeignKey("promotions.id"))

    __table_args__ = (
        PrimaryKeyConstraint("customer_id", "payment_id", "promotion_id"),
        {},
    )

    customers = relationship("Customer", back_populates="customers_payments_promotions")
    payments = relationship("Payment", back_populates="customers_payments_promotions")
    promotions = relationship("Promotion", back_populates="customers_payments_promotions")
