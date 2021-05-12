from datetime import date
from decimal import Decimal

from pydantic import BaseModel

from . import BaseClassModel


class ProductListModel(BaseClassModel):
    name: str
    price: Decimal
    create_product_date: date


class OrderListModel(BaseClassModel):
    id_product: int
    name_product: str
    price_order: Decimal
    status_order: str
    create_order_date: date


class CreateOrderModel(BaseModel):
    product_id: int


class CreateCheckModel(BaseModel):
    order_id: int


class CheckListModel(BaseClassModel):
    id_order: int
    name_product: str
    price_to_pay: Decimal
    create_check_date: date
