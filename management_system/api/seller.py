from typing import List

from fastapi import APIRouter, Depends

from ..models.seller import OrderListModel
from ..services.seller import SellerService


router = APIRouter(
    prefix="/seller",
    tags=["Продавец-консультант"]
)


@router.get("/orders_new", response_model=List[OrderListModel])
def get_orders_status_new(service: SellerService = Depends()):
    return service.get_orders()


@router.put("/order_completed/{order_id}", response_model=OrderListModel)
def update_status_order(
        order_id: int,
        service: SellerService = Depends()
):
    return service.update_status_order(order_id)
