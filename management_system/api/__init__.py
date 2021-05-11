from fastapi import APIRouter

from .cashier import router as cashier_router
from .products import router as product_router
from .seller import router as seller_router
from .accountant import router as accountant_router


# корневой роутер
router = APIRouter()

# подключение роутеров
router.include_router(product_router)
router.include_router(cashier_router)
router.include_router(seller_router)
router.include_router(accountant_router)
