from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Extra, conlist, conint, validator
from uuid import UUID


class Status(Enum):
    created = 'created'
    progress = 'progress' 
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered' 


class Size(Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'


class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[conint(ge=1, strict=True)] = 1

    class Config:
        extra = Extra.forbid

    @validator("quantity")
    def quantity_non_nullable(cls, value):
        if value is None:
            raise ValueError('quantity may not bе None')
        
        return value

class CreateOrderSchema(BaseModel):
    order: conlist(OrderItemSchema, min_items=1)

    class Config:
        extra = Extra.forbid


class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: Status

class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]