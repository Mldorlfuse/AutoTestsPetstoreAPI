from api.base_api import BaseAPI
import allure
from faker import Faker

fake = Faker()

class UserAPI(BaseAPI):
    def create_user(self, user_data):
        with allure.step(f'Создание нового пользователя с id {user_data["id"]}'):
            headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
            body = user_data
            return self.post('/user', json=body, headers=headers)

    def get_user(self, username):
        with allure.step(f'Поиск пользователя с username {username}'):
            headers = {'accept': 'application/json'}
            return self.get(f'/user/{username}', headers=headers)

    def update_user(self, username, new_user_data):
        with allure.step(f'Изменение данных пользователя с username {username}'):
            headers = {'accept': 'application/json'}
            body = new_user_data
            return self.put(f'/user/{username}', json=body, headers=headers)

    def delete_user(self, username):
        with allure.step(f'Удаление пользователя с username {username}'):
            headers = {'accept': 'application/json'}
            return self.delete(f'/user/{username}', headers=headers)

    def login_user(self, username, password):
        with allure.step(f'Логин пользователя с username {username}'):
            headers = {'accept': 'application/json'}
            return self.get(f'/user/login?username={username}&password={password}', headers=headers)

    def logout_user(self):
        with allure.step('Логаут пользователя'):
            headers = {'accept': 'application/json'}
            return self.get(f'/user/logout', headers=headers)

    def array_users(self,count):
        array_users = []
        for i in range(count):
            user_data = {
                "id": fake.random_int(min=10000, max=99999),
                "username": fake.user_name(),
                "firstName": fake.first_name(),
                "lastName": fake.last_name(),
                "email": fake.email(),
                "password": fake.password(),
                "phone": fake.phone_number(),
                "userStatus": fake.random_int(min=1, max=3),
            }
            array_users.append(user_data)
        return array_users

    def new_array_users(self,count):
        new_array_users = []
        for i in range(count):
            user_data = {
                "id": fake.random_int(min=10000, max=99999),
                "username": fake.user_name(),
                "firstName": fake.first_name(),
                "lastName": fake.last_name(),
                "email": fake.email(),
                "password": fake.password(),
                "phone": fake.phone_number(),
                "userStatus": fake.random_int(min=1, max=3),
            }
            new_array_users.append(user_data)
        return new_array_users

    def create_list_users(self, array_users, count):
        with allure.step(f'Создание пользователей в количестве {count}'):
            headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
            body = array_users
            return self.post('/user/createWithList', json=body, headers=headers)

    def check_after_create_user(self, response, user_id):
        with allure.step(f'Проверка создания пользователя с id {user_id}'):
            with allure.step('Статус кода ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'В теле ответа есть созданный id {user_id}'):
                assert int(response.json()['message']) == user_id

    def check_after_get_user(self, response, user_data):
        with allure.step(f'Поиск пользователя с username {user_data["username"]}'):
            with allure.step('Статус кода ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'id пользователя из ответа {response.json()["id"]} равен созданному id {user_data["id"]}'):
                assert response.json()['id'] == user_data['id']
            with allure.step(f'username пользователя из ответа {response.json()["username"]} равен созданному username {user_data["username"]}'):
                assert response.json()['username'] == user_data['username']
            with allure.step(f'firstName пользователя из ответа {response.json()["firstName"]} равен созданному firstName {user_data["firstName"]}'):
                assert response.json()['firstName'] == user_data['firstName']
            with allure.step(f'lastName пользователя из ответа {response.json()["lastName"]} равен созданному lastName {user_data["lastName"]}'):
                assert response.json()['lastName'] == user_data['lastName']
            with allure.step(f'email пользователя из ответа {response.json()["email"]} равен созданному email {user_data["email"]}'):
                assert response.json()['email'] == user_data['email']
            with allure.step(f'password пользователя из ответа {response.json()["password"]} равен созданному password {user_data["password"]}'):
                assert response.json()['password'] == user_data['password']
            with allure.step(f'phone пользователя из ответа {response.json()["phone"]} равен созданному phone {user_data["phone"]}'):
                assert response.json()['phone'] == user_data['phone']
            with allure.step(f'userStatus пользователя из ответа {response.json()["userStatus"]} равен созданному userStatus {user_data["userStatus"]}'):
                assert response.json()['userStatus'] == user_data['userStatus']

    def check_after_update_user(self, response, user_id):
        with allure.step(f'Проверка изменения пользователя с id {user_id}'):
            with allure.step('Статус кода ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'В теле ответа есть изменяемый id {user_id}'):
                assert int(response.json()['message']) == user_id

    def check_after_delete_user(self, response, username):
        with allure.step(f'Проверка изменения пользователя с username {username}'):
            with allure.step('Статус кода ответа равен 200'):
                assert response.status_code == 200
            with allure.step(f'В теле ответа есть удаляемый username {username}'):
                assert response.json()['message'] == username

    def check_get_user_after_delete(self, response, username):
        with allure.step(f'Поиск пользователя с username {username} после удаления'):
            with allure.step('Статус кода ответа равен 404'):
                assert response.status_code == 404

    def check_after_login_user(self, response, username):
        with allure.step(f'Проверка логина пользователя с username {username}'):
            with allure.step('Статус кода ответа равен 200'):
                assert response.status_code == 200
            with allure.step('В теле ответа есть информация об успешном логине'):
                assert response.json()['message'][:14] == 'logged in user'

    def check_after_logout_user(self, response):
        with allure.step(f'Проверка логаута пользователя'):
            with allure.step('Статус кода ответа равен 200'):
                assert response.status_code == 200
            with allure.step('В теле ответа есть информация об успешном логауте'):
                assert response.json()['message'][:2] == 'ok'

    def check_after_create_list_users(self, response, count):
        with allure.step(f'Проверка создания пользователей в количестве {count}'):
            with allure.step('Статус кода ответа равен 200'):
                assert response.status_code == 200
            with allure.step('В теле ответа есть информация об успешном создании'):
                assert response.json()['message'][:2] == 'ok'