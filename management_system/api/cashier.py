from typing import List

from fastapi import APIRouter, Depends

from ..models.cashier import ProductListModel, CreateOrderModel, OrderListModel, CheckListModel, CreateCheckModel
from ..services.cashier import CashierService


router = APIRouter(
    prefix="/cashier",
)


@router.get("/products", response_model=List[ProductListModel])
def get_product_list(service: CashierService = Depends()):
    return service.get_products_list()


@router.post("/create-order")
def create_order(
        product_data: CreateOrderModel,
        service: CashierService = Depends()
):
    return service.create_order(product_data.product_id)


@router.get("/orders_completed", response_model=List[OrderListModel])
def get_orders_list(service: CashierService = Depends()):
    return service.get_list_order_completed()


@router.post("/create_check", response_model=CheckListModel)
def create_check(
        order_data: CreateCheckModel,
        service: CashierService = Depends()
):
    return service.create_check(order_data.order_id)


@router.get("/checks", response_model=List[CheckListModel])
def get_checks(service: CashierService = Depends()):
    return service.get_checks()


@router.put("/check_close/{check_id}", response_model=CheckListModel)
def close_check(
        check_id: int,
        service: CashierService = Depends()
):
    return service.check_close(check_id)
