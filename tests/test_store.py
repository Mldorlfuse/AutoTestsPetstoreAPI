import allure



@allure.epic("Petstore API")
@allure.feature("Store")
@allure.story("Получение списка запасов и проверка количества проданных и остатков")
def test_inventory(store_api):

    response_inventory = store_api.get_inventory()
    store_api.check_inventory(response_inventory)

@allure.epic("Petstore API")
@allure.feature("Store")
@allure.story("Создание нового заказа и проверка")
def test_new_order(store_api, create_order, store_order_data):

    response_get_order = store_api.get_order(create_order.json()['id'])
    store_api.check_new_order(create_order, store_order_data)
    store_api.check_get_order(response_get_order, store_order_data)

@allure.epic("Petstore API")
@allure.feature("Store")
@allure.story("Удаление заказа")
def test_delete_order(store_api, create_order):

    response_delete_order = store_api.delete_order(create_order.json()['id'])
    store_api.check_delete_order(response_delete_order, create_order.json()['id'])
    response_get_order = store_api.get_order(create_order.json()['id'])
    store_api.check_oreder_after_delete(response_get_order, create_order.json()['id'])