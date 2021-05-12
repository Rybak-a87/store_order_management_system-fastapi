from typing import List

from fastapi import APIRouter, Depends

from ..models.cashier import ProductListModel, CreateOrderModel, OrderListModel, CheckListModel, CreateCheckModel
from ..services.cashier import CashierService


router = APIRouter(
    prefix="/cashier",
    tags=["Кассир"]
)


@router.get("/products", response_model=List[ProductListModel])
def get_product_list(service: CashierService = Depends()):
    """
    ## Получение списка товаров
    """
    return service.get_products_list()


@router.post("/create-order", response_model=OrderListModel)
def create_order(
        product_data: CreateOrderModel,
        service: CashierService = Depends()
):
    """
    ## Создание заказа по указанному номеру (id) товара
    """
    return service.create_order(product_data.product_id)


@router.get("/orders_completed", response_model=List[OrderListModel])
def get_orders_list(service: CashierService = Depends()):
    """
    ## Получение списка заказов которые обработанны продавцом-консультантом (выполненные)
    """
    return service.get_list_order_completed()


@router.post("/create_check", response_model=CheckListModel)
def create_check(
        order_data: CreateCheckModel,
        service: CashierService = Depends()
):
    """
    ## Генерация счета на выполненныйй заказ
    """
    return service.create_check(order_data.order_id)


@router.get("/checks", response_model=List[CheckListModel])
def get_checks(service: CashierService = Depends()):
    """
    ## Полугчение спичка открытых (не оплоченных) счетов
    """
    return service.get_checks()


@router.put("/check_close/{check_id}", response_model=CheckListModel)
def close_check(
        check_id: int,
        service: CashierService = Depends()
):
    """
    ## Зактытие счета (счет оплачен)
    """
    return service.check_close(check_id)
