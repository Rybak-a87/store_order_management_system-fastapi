# ---
# описание таблиц базы данных
# ---
from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()


class ProductDB(Base):
    """модель товара с бд"""
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    price = Column(Numeric(10, 2))
    create_product_date = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f"Идинтификатор товара: {self.id}"


class OrderDB(Base):
    """модель заказа с бд"""
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, unique=True)
    id_product = Column(Integer)
    name_product = Column(String)
    price_order = Column(Numeric(10, 2))
    create_order_date = Column(DateTime(timezone=True), default=func.now())
    status_order = Column(String, default="new")
    status_check = Column(Boolean, default=False)

    def __repr__(self):
        return f"Номер заказа: {self.id}"


class CheckDB(Base):
    """модель счета с бд"""
    __tablename__ = "check"
    id = Column(Integer, primary_key=True, unique=True)
    id_order = Column(Integer)
    name_product = Column(String)
    price_to_pay = Column(Numeric(10, 2))
    create_check_date = Column(DateTime(timezone=True), default=func.now())
    status_pay = Column(Boolean, default=False)

    def __repr__(self):
        return f"Номер счета: {self.id}"


# создание базы данных
# from management_system.database.conf_db import engine
# Base.metadata.create_all(engine)
