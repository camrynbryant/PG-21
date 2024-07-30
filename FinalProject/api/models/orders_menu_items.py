from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class OrderMenuItem:
    __tablename__ = "orders_menu_items"

    order_id = Column(Integer, ForeignKey("orders.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))

    __table_args__ = (
        PrimaryKeyConstraint("order_id", "menu_item_id"),
        {},
    )

    orders = relationship("Order", back_populates="orders_menu_items")
    menu_items = relationship("MenuItem", back_populates="orders_menu_items")
