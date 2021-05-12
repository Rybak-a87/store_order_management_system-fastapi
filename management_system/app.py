# основной файл приложения
from fastapi import FastAPI

from .api import router


tags_metadata = [
    {
        "name": "Кассир",
        "description": "Добавляет заказ, генерирует счет, закрывает счет и заказ"
    },
    {
        "name": "Продавец-консультант",
        "description": "Обрабатывает заказ, меняет статус заказа"
    },
    {
        "name": "Бухгалтер",
        "description": "Просматривает все заказы. Может выбирать диапозон создания заказов (например с 01.07.2021 до 31.07.2021)"
    },
]


app = FastAPI(
    title="Store order management system",
    description="Система управления заказами в магазине",
    version="1.0.0",
    openapi_tags=tags_metadata
)

app.include_router(router=router)
