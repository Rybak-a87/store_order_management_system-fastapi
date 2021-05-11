from fastapi import APIRouter, Depends

from ..models.products import CreateProductModel
from ..models.cashier import ProductListModel
from ..services.products import ProductService

router = APIRouter(
    prefix="/create-product"
)


@router.post("/")
def create_product(
        product_data: CreateProductModel,
        service: ProductService = Depends()
):
    return service.create_product(product_data)
