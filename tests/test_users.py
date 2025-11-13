import allure



@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Создание и проверка пользователя")
def test_create_user(create_user, user_api, user_data):

    user_api.check_after_create_user(create_user, user_data['id'])
    response_get_user = user_api.get_user(user_data['username'])
    user_api.check_after_get_user(response_get_user, user_data)

@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Изменение данных и проверка пользователя")
def test_update_user(create_user, user_api, user_data, new_user_data):

    response_update_user = user_api.update_user(user_data['username'], new_user_data)
    user_api.check_after_update_user(response_update_user, new_user_data['id'])
    response_get_user = user_api.get_user(new_user_data['username'])
    user_api.check_after_get_user(response_get_user, new_user_data)

@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Удаление пользователя и проверка")
def test_delete_user(create_user, user_api, user_data):

    response_delete_user = user_api.delete_user(user_data['username'])
    user_api.check_after_delete_user(response_delete_user, user_data['username'])
    response_get_user = user_api.get_user(user_data['username'])
    user_api.check_get_user_after_delete(response_get_user, user_data['username'])

@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Проверка Логина и Логаута пользователя")
def test_login_and_logout(create_user, user_api, user_data):

    response_user_login = user_api.login_user(user_data['username'], user_data['password'])
    user_api.check_after_login_user(response_user_login, user_data['username'])
    response_user_logout = user_api.logout_user()
    user_api.check_after_logout_user(response_user_logout)

@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Создание нескольких пользователей с помощью списка и проверка")
def test_create_list_users_with_count(create_user, user_api, get_random_user_count):

    count = get_random_user_count
    created_users = user_api.array_users(count)

    response_create_list_users = user_api.create_list_users(created_users, count)
    user_api.check_after_create_list_users(response_create_list_users, count)
    for i in range(count):
        response_get_user = user_api.get_user(created_users[i]['username'])
        user_api.check_after_get_user(response_get_user, created_users[i])

@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Создание нескольких пользователей с помощью списка, удаление и проверка")
def test_delete_list_users_with_count(create_user, user_api, get_random_user_count):

    count = get_random_user_count
    created_users = user_api.array_users(count)

    user_api.create_list_users(created_users, count)
    for i in range(count):
        test_delete_user(create_user='',user_api=user_api, user_data=created_users[i])

@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Создание нескольких пользователей с помощью списка, изменение и проверка")
def test_update_list_users_with_count(create_user, user_api, get_random_user_count):

    count = get_random_user_count
    created_users = user_api.array_users(count)
    new_created_users = user_api.new_array_users(count)

    user_api.create_list_users(created_users, count)
    for i in range(count):
        test_update_user(create_user='', user_api=user_api, user_data=created_users[i], new_user_data=new_created_users[i])

@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Создание нескольких пользователей с помощью списка и проверка возможности логина и логаута для каждого")
def test_login_and_logout_list_users_with_count(create_user, user_api, get_random_user_count):

    count = get_random_user_count
    created_users = user_api.array_users(count)

    user_api.create_list_users(created_users, count)
    for i in range(count):
        test_login_and_logout(create_user='', user_api=user_api, user_data=created_users[i])