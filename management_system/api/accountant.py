from typing import List, Optional
from datetime import date, datetime

from fastapi import APIRouter, Depends

from ..models.accountant import OrderListModel
from ..services.accountant import AccountantService


router = APIRouter(
    prefix="/accountant"
)


@router.get("/orders", response_model=List[OrderListModel])
def get_order_list(
        date_start: Optional[str] = None,
        date_end: Optional[str] = None,
        service: AccountantService = Depends()
):
    return service.get_orders(date_start, date_end)
