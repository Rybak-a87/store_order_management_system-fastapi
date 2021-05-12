from fastapi import APIRouter, Depends

from ..models.products import CreateProductModel
from ..models.cashier import ProductListModel
from ..services.products import ProductService

router = APIRouter(
    prefix="/create-product",
    tags=["Создание товара"]
)


@router.post("/", response_model=ProductListModel)
def create_product(
        product_data: CreateProductModel,
        service: ProductService = Depends()
):
    """
    ## Добавить товар в базу данных
    \f
    :param product_data:
    :param service:
    :return:
    """
    return service.create_product(product_data)
