from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database.conf_db import get_session
from ..database import tables
from ..models.seller import OrderListModel


class SellerService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_orders(self) -> List[tables.OrderDB]:
        """возвращает заказы со статусом <new>"""
        orders = self.session.query(tables.OrderDB).filter_by(status_order="new").all()
        return orders

    def update_status_order(self, order_id: int) -> tables.OrderDB:
        """меняет статус заказа на выполненный <completed>"""
        order = self.session.query(tables.OrderDB).filter_by(id=order_id).first()
        if not order or order.status_order != "new":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        order.status_order = "completed"
        self.session.commit()
        return order
