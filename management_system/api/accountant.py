from typing import List, Optional
from datetime import date, datetime

from fastapi import APIRouter, Depends

from ..models.accountant import OrderListModel
from ..services.accountant import AccountantService


router = APIRouter(
    prefix="/accountant",
    tags=["Бухгалтер"]
)


@router.get("/orders", response_model=List[OrderListModel])
def get_order_list(
        date_start: Optional[str] = None,
        date_end: Optional[str] = None,
        service: AccountantService = Depends()
):
    """
    ## Получение списка заказов с возможностью выбора промежутка времени (в формате <число>.<месяц>.<год>)
    \f
    :param date_start:
    :param date_end:
    :param service:
    :return:
    """
    return service.get_orders(date_start, date_end)
