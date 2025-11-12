from .base_api import BaseAPI
import os
import allure

class PetAPI(BaseAPI):

    def add_image_to_pet(self, pet_id, file_path):
        with allure.step(f'Загрузка файла {os.path.basename(file_path)} к питомцу'):
            headers = {'accept': 'application/json'}
            with open(file_path, 'rb') as f:
                files = {'file': (os.path.basename(file_path), f, 'image/png')}
                return self.post(f'/pet/{pet_id}/uploadImage', headers=headers, files=files)

    def add_pet(self, pet_data):
        with allure.step(f'Создание нового питомца с id {pet_data["id"]}'):
            body = pet_data
            headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
            return self.post('/pet', json=body, headers=headers)

    def get_pet(self, pet_id):
        with allure.step(f'Поиск питомца с id {pet_id}'):
            headers = {'accept': 'application/json'}
            return self.get(f"/pet/{pet_id}", headers=headers)

    def update_pet(self, pet_data, new_pet_data):
        with allure.step(f'Обновление имени питомца на {new_pet_data["name"]} и статуса на {new_pet_data["status"]}'):
            headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
            body = {
                'id': pet_data['id'],
                'name': new_pet_data['name'],
                'status': new_pet_data['status'],
            }
            return self.put('/pet', json=body, headers=headers)

    def find_pet_by_status(self, pet_status):
        with allure.step(f'Поиск питомцев с статусом {pet_status}'):
            headers = {'accept': 'application/json'}
            return self.get(f'/pet/findByStatus?status={pet_status}', headers=headers)

    def update_pet_by_id(self, pet_id, new_pet_data):
        with allure.step(f'Обновление имени питомца с id {pet_id} на {new_pet_data["name"]} и статуса на {new_pet_data["status"]}'):
            data = {
                'name': new_pet_data['name'],
                'status': new_pet_data['status']
            }
            headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
            return self.post(f'/pet/{pet_id}', data=data, headers=headers)

    def delete_pet(self, pet_id):
        with allure.step(f'Удаление питомца с id {pet_id}'):
            headers = {'accept':'application/json'}
            return self.delete(f'/pet/{pet_id}', headers=headers)

    def check_pet_after_create(self, response, pet_data):
        with allure.step('Проверка после создания'):
            with allure.step('Код ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'Id питомца из ответа {response.json()["id"]} равен отправленному id {pet_data["id"]}'):
                assert response.json()['id'] == pet_data['id']
            with allure.step(f'Имя питомца из ответа {response.json()["name"]} равен отправленному имени {pet_data["name"]}'):
                assert response.json()['name'] == pet_data['name']
            with allure.step(f'Статус питомца из ответа {response.json()["status"]} равен отправленному статусу {pet_data["status"]}'):
                assert response.json()['status'] == pet_data['status']

    def check_pet_after_get(self, response, pet_data):
        with allure.step('Проверка после поиска'):
            with allure.step('Код ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'id питомца из ответа {response.json()["id"]} равен созданному id {pet_data["id"]}'):
                assert response.json()['id'] == pet_data['id']
            with allure.step(f'Имя питомца из ответа {response.json()["name"]} равен созданному имени {pet_data["name"]}'):
                assert response.json()['name'] == pet_data['name']
            with allure.step(f'Статус питомца из ответа {response.json()["status"]} равен созданному статусу {pet_data["status"]}'):
                assert response.json()['status'] == pet_data['status']

    def check_pet_after_upload_image(self, response, file_name):
        with allure.step('Проверка статуса кода ответа и тела ответа'):
            with allure.step('Код ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'Файл {file_name} есть в ответе'):
                assert file_name in response.json()['message']

    def check_pet_after_update(self, response, new_pet_data):
        with allure.step('Проверка после изменения'):
            with allure.step('Код ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'Имя питомца из ответа {response.json()["name"]} равен новому имени {new_pet_data["name"]}'):
                assert response.json()['name'] == new_pet_data['name']
            with allure.step(f'Статус питомца из ответа {response.json()["status"]} равен новому статусу {new_pet_data["status"]}'):
                assert response.json()['status'] == new_pet_data['status']

    def check_pet_after_find_by_status(self, response,response_find_by_status, pet_status):
        with allure.step(f'Проверка после поиска по статусу {pet_status}'):
            with allure.step('Код ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'В ответе есть данные созданного питомца с id {response.json()["id"]}'):
                assert response.json() in response_find_by_status.json()

    def check_pet_after_update_by_id(self, response, pet_id):
        with allure.step(f'Проверка после изменения данных питомца по id {pet_id}'):
            with allure.step('Код ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'В ответе есть данные созданного питомца с id {pet_id}'):
                assert str(pet_id) == response.json()['message']

    def check_pet_after_delete(self, response, pet_id, get_pet_status):
        with allure.step(f'Проверка после удаления данных питомца по id {pet_id}'):
            with allure.step('Код ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'В ответе есть данные удаленного питомца с id {pet_id}'):
                assert str(pet_id) == response.json()['message']
            with allure.step(f'Код ответа равен 404 при поиске удаленного питомца'):
                assert get_pet_status.status_code == 404