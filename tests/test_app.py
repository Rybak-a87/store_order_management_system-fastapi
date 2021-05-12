"""
PS.
С тестами у меня трудности, мало времени на них оставил
нужна помощь в этом вопросе
"""
from fastapi.testclient import TestClient

from management_system.app import app


client = TestClient(app)

test_product = {
    "name": "test_product",
    "price": 1000
}

test_order = {
    "product_id": 1,
}

test_check = {
    "order_id": 1
}


def test_create_product():
    """
    добавление товара в базу данных
    """
    response = client.post("/create-product", json=test_product)
    assert response.status_code == 200
    assert response.json()


def test_get_list_product():
    """
    получение списка товаров
    """
    response = client.get("/cashier/products/")
    assert response.status_code == 200
    assert response.json()


def test_create_order():
    """
    создание заказа по id товара
    """
    response = client.post("/cashier/create-order/", json=test_order)
    assert response.status_code == 200
    assert response.json()


def test_get_list_order_new():
    """
    получение списка заказов со статусом new
    """
    response = client.get("/seller/orders_new/")
    assert response.status_code == 200
    assert response.json()


def test_get_list_order_completed():
    """
    получение списка заказов со статусом completed
    """
    response = client.get("/cashier/orders_completed/")
    assert response.status_code == 200
    assert response.json()


def test_get_list_all_order():
    """
    получение списка всех заказов
    """
    response = client.get("/accountant/orders/")
    assert response.status_code == 200
    assert response.json()


def test_create_check():
    """
    генерация счета на выполненный заказ
    """
    response = client.post("/cashier/create_check/", json=test_check)
    assert response.status_code == 200
    assert response.json()


def test_get_list_check():
    """
    получение спичка открытых счетов
    """
    response = client.get("/cashier/checks/")
    assert response.status_code == 200
    assert response.json()
