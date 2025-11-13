from .base_api import BaseAPI
import allure

class StoreAPI(BaseAPI):
    def get_inventory(self):
        with allure.step('Получение списка запасов'):
            headers = {'accept': 'application/json'}
            return self.get('/store/inventory', headers=headers)

    def new_order(self, order_data):
        with allure.step(f'Создание нового заказа с id {order_data["id"]}'):
            headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
            body = order_data
            return self.post('/store/order', headers=headers, json=body)

    def get_order(self, order_id):
        with allure.step(f'Получить заказ по id {order_id}'):
            headers = {'accept': 'application/json'}
            return self.get(f'/store/order/{order_id}', headers=headers)

    def delete_order(self, order_id):
        with allure.step(f'Удалить заказ с id {order_id}'):
            headers = {'accept': 'application/json'}
            return self.delete(f'/store/order/{order_id}', headers=headers)

    def check_inventory(self, response):
        with allure.step('Проверка запасов'):
            with allure.step('Код ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'Проданных товаров {response.json()["sold"]} больше 0'):
                assert int(response.json()['sold']) > 0
            with allure.step(f'Остатков {response.json()["available"]} больше 0'):
                assert response.json()['available'] > 0

    def check_new_order(self, response, order_data):
        with allure.step('Проверка созданного заказа'):
            with allure.step('Код ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'Id заказа из ответа {response.json()["id"]} равен отправленному id {order_data["id"]}'):
                assert response.json()['id'] == order_data['id']
            with allure.step(f'Id питомца заказа из ответа {response.json()["petId"]} равен отправленному Id питомца {order_data["petId"]}'):
                assert response.json()['petId'] == order_data['petId']
            with allure.step(f'Количество в заказе из ответа {response.json()["quantity"]} равен отправленному количеству {order_data["quantity"]}'):
                assert response.json()['quantity'] == order_data['quantity']
            with allure.step(f'Дата заказа из ответа {response.json()["shipDate"]} равна отправленному дате заказа {order_data["shipDate"]}'):
                assert str(response.json()['shipDate'][:-5]) == str(order_data['shipDate'])[:-1]
            with allure.step(f'Статус заказа из ответа {response.json()["status"]} равен отправленному статусу {order_data["status"]}'):
                assert response.json()['status'] == order_data['status']
            with allure.step(f'Завершенность заказа из ответа {response.json()["complete"]} равна отправленной завершенности {order_data["complete"]}'):
                assert str(response.json()['complete']).lower() == order_data['complete']

    def check_get_order(self, response, order_data):
        with allure.step('Проверка полученного'):
            with allure.step('Код ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'Id заказа из ответа {response.json()["id"]} равен созданному id {order_data["id"]}'):
                assert response.json()['id'] == order_data['id']
            with allure.step(f'Id питомца заказа из ответа {response.json()["petId"]} равен созданному Id питомца {order_data["petId"]}'):
                assert response.json()['petId'] == order_data['petId']
            with allure.step(f'Количество в заказе из ответа {response.json()["quantity"]} равен созданному количеству {order_data["quantity"]}'):
                assert response.json()['quantity'] == order_data['quantity']
            with allure.step(f'Дата заказа из ответа {response.json()["shipDate"]} равна созданной дате заказа {order_data["shipDate"]}'):
                assert str(response.json()['shipDate'][:-5]) == str(order_data['shipDate'])[:-1]
            with allure.step(f'Статус заказа из ответа {response.json()["status"]} равен созданному статусу {order_data["status"]}'):
                assert response.json()['status'] == order_data['status']
            with allure.step(f'Завершенность заказа из ответа {response.json()["complete"]} равна созданной завершенности {order_data["complete"]}'):
                assert str(response.json()['complete']).lower() == order_data['complete']

    def check_delete_order(self, response, order_id):
        with allure.step(f'Проверка удаления заказа с id {order_id}'):
            with allure.step('Код ответа равен 200'):
                assert response.status_code == 200
            with allure.step('id удаленного элемента есть в коде ответа'):
                assert response.json()['message'] == str(order_id)

    def check_oreder_after_delete(self, response, order_id):
        with allure.step(f'Проверка отсутствия заказа с id {order_id} после удаления'):
            with allure.step('Код ответа равен 404'):
                assert response.status_code == 404