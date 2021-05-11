from fastapi import Depends
from sqlalchemy.orm import Session

from ..database import tables
from ..database.conf_db import get_session
from ..models.products import CreateProductModel


class ProductService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_product(self, product_data: CreateProductModel) -> tables.ProductDB:
        product = tables.ProductDB(
            name=product_data.name,
            price=product_data.price
        )
        self.session.add(product)
        self.session.commit()
        return product
