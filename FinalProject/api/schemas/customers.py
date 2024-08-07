from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List


class CustomerBase(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    email: Optional[str] = Field(None, max_length=50)
    phone_number: Optional[str] = Field(None, max_length=20)
    address: Optional[str] = Field(None, max_length=100)


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    email: Optional[str] = Field(None, max_length=50)
    phone_number: Optional[str] = Field(None, max_length=20)
    address: Optional[str] = Field(None, max_length=100)


class Customer(CustomerBase):
    id: int
    class ConfigDict:
        from_attributes = True
