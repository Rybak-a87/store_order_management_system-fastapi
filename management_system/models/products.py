from decimal import Decimal

from pydantic import BaseModel


class CreateProductModel(BaseModel):
    name: str
    price: Decimal
