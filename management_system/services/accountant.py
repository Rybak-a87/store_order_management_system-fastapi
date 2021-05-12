from typing import List, Optional
from datetime import date

from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import and_

from ..database.conf_db import get_session
from ..database import tables
from ..models.accountant import OrderListModel


class AccountantService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    @staticmethod
    def format_date(str_date) -> date:
        temp_date = str_date.split(".")
        try:
            new_date = date(
                int(temp_date[2]),
                int(temp_date[1]),
                int(temp_date[0])
            )
        except:
            new_date = None
        return new_date

    def get_orders(self, date_start: Optional[str] = None, date_end: Optional[str] = None) -> List[OrderListModel]:
        query = self.session.query(tables.OrderDB)
        if date_end and date_start:
            query = query.filter(and_(tables.OrderDB.create_order_date >= self.format_date(date_start), tables.OrderDB.create_order_date <= self.format_date(date_end)))
        orders = query.all()
        return orders
