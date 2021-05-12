from datetime import datetime
from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import tables
from ..database.conf_db import get_session
from ..models.cashier import ProductListModel, OrderListModel


class CashierService:
    """представления кассира"""
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    @staticmethod
    def __sale(price, create_date):
        """применение скидки если товару больше 30 дней"""
        sale = 20    # % скидка
        if abs(datetime.toordinal(datetime.utcnow()) - datetime.toordinal(create_date)) > 30:
            return price - (price*sale/100)
        return price

    def _get_product(self, id_product: int) -> tables.ProductDB:
        """возвращает продук по его id"""
        product = self.session.query(tables.ProductDB).filter_by(id=id_product).first()
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return product

    def _get_order(self, id_order: int) -> tables.OrderDB:
        """выводит заказ по id"""
        order = self.session.query(tables.OrderDB).filter_by(id=id_order).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return order

    def get_products_list(self) -> List[tables.ProductDB]:
        """возвращает список продуктов"""
        products = self.session.query(tables.ProductDB).all()
        return products

    def create_order(self, product_id: int) -> tables.OrderDB:
        """создание заказа"""
        product = self._get_product(product_id)
        order = tables.OrderDB(
            id_product=product.id,
            name_product=product.name,
            price_order=self.__sale(product.price, product.create_product_date)
        )
        self.session.add(order)
        self.session.commit()
        return order

    def get_list_order_completed(self) -> List[tables.OrderDB]:
        """возвращаеть заказы со статусом <выполненно>"""
        orders = self.session.query(tables.OrderDB).filter_by(status_order="completed", status_check=False).all()
        return orders

    def get_checks(self) -> List[tables.CheckDB]:
        """возвращает не оплаченные счета """
        checks = self.session.query(tables.CheckDB).filter_by(status_pay=False).all()
        return checks

    def create_check(self, order_id: int) -> tables.CheckDB:
        """создание счета"""
        order = self.session.query(tables.OrderDB).filter_by(id=order_id).first()
        if not order or order.status_order != "completed":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        check = tables.CheckDB(
            id_order=order.id,
            name_product=order.name_product,
            price_to_pay=order.price_order
        )
        order.status_check = True
        self.session.add(check)
        self.session.commit()
        return check

    def check_close(self, check_id: int) -> tables.CheckDB:
        """закрытие счета - счет оплачен"""
        check = self.session.query(tables.CheckDB).filter_by(id=check_id).first()
        if not check or check.status_pay:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        order = self.session.query(tables.OrderDB).filter_by(id=check.id_order).first()
        order.status_order = "payed"
        check.status_pay = True
        self.session.commit()
        return check

