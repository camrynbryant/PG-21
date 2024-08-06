from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List


class CustomerBase(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr] = Field(None, max_length=50)
    phone_number: Optional[str] = Field(None, max_length=20)
    address: Optional[str] = Field(None, max_length=100)


class CustomerCreate(CustomerBase):
    name: str
    email: EmailStr


class CustomerUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr] = Field(None, max_length=50)
    phone_number: Optional[str] = Field(None, max_length=20)
    address: Optional[str] = Field(None, max_length=100)


class Review(BaseModel):
    # Define the fields for the Review model here
    id: int
    review_text: str
    rating: int
    customer_id: int

    class Config:
        orm_mode = True


class Order(BaseModel):
    # Define the fields for the Order model here
    id: int
    order_date: str
    order_amount: float
    customer_id: int

    class Config:
        orm_mode = True


class CustomerPaymentPromotion(BaseModel):
    # Define the fields for the CustomerPaymentPromotion model here
    id: int
    payment_id: int
    promotion_id: int
    customer_id: int

    class Config:
        orm_mode = True


class Customer(CustomerBase):
    id: int
    reviews: List[Review] = []
    orders: List[Order] = []
    customers_payments_promotions: List[CustomerPaymentPromotion] = []

    class Config:
        orm_mode = True
