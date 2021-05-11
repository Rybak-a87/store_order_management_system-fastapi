from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class ProductListModel(BaseModel):
    id: int
    name: str
    price: Decimal
    create_date: date

    class Config:
        orm_mode = True


class OrderListModel(BaseModel):
    id: int
    id_product: int
    name_product: str
    price_order: Decimal
    status_order: str
    create_date: date

    class Config:
        orm_mode = True


class CreateOrderModel(BaseModel):
    product_id: int


class CreateCheckModel(BaseModel):
    order_id: int


class CheckListModel(BaseModel):
    id: int
    id_order: int
    name_product: str
    price_to_pay: Decimal
    create_date: date

    class Config:
        orm_mode = True
