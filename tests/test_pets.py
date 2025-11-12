import os
import allure

@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("Создание и поиск созданного питомца")
def test_create_and_find_pet(create_pet, pet_api, pet_data, file_path):

    pet_api.check_pet_after_create(create_pet, pet_data)
    response_get_pet = pet_api.get_pet(create_pet.json()['id'])
    pet_api.check_pet_after_get(response_get_pet, pet_data)

@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("Добавление картинки к питомцу")
def test_upload_image_to_pet(create_pet, pet_api, pet_data, file_path):

    response_add_image_to_pet = pet_api.add_image_to_pet(create_pet.json()['id'], file_path)
    file_name = os.path.basename(file_path)
    pet_api.check_pet_after_upload_image(response_add_image_to_pet, file_name)

@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("Изменение данных питомца и проверка измененных данных")
def test_update_pet(create_pet, pet_api, new_pet_data):

    response_update_pet = pet_api.update_pet(create_pet.json(), new_pet_data)
    pet_api.check_pet_after_update(response_update_pet, new_pet_data)
    response_get_pet = pet_api.get_pet(response_update_pet.json()['id'])
    pet_api.check_pet_after_get(response_get_pet, response_update_pet.json())

@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("Поиск питомца по статусу")
def test_find_by_status_pet(create_pet, pet_api, pet_data):

    response_find_by_status = pet_api.find_pet_by_status(pet_data['status'])
    pet_api.check_pet_after_find_by_status(create_pet, response_find_by_status, pet_data['status'])

# Ооооочнь редко срабатывает

@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("Изменение питомца по id")
def test_update_pet_by_id(create_pet, pet_api, pet_data, new_pet_data):

    response_update_by_id = pet_api.update_pet_by_id(create_pet.json()['id'], new_pet_data)
    response_get_pet = pet_api.get_pet(create_pet.json()['id'])
    update_pet_data = {
        'id': create_pet.json()['id'],
        'name': new_pet_data['name'],
        'status': new_pet_data['status']
    }
    pet_api.check_pet_after_get(response_get_pet, update_pet_data)
    pet_api.check_pet_after_update_by_id(response_update_by_id, update_pet_data['id'])

@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("Удаление питомца по id")
def test_delete_pet(create_pet, pet_api):
    
    response_delete = pet_api.delete_pet(create_pet.json()['id'])
    response_get_pet = pet_api.get_pet(create_pet.json()['id'])
    pet_api.check_pet_after_delete(response_delete, create_pet.json()['id'], response_get_pet)
