import pytest
import os
from faker import Faker
from api.pet_api import PetAPI
from api.store_api import StoreAPI
# from api.user_api import UserAPI
from datetime import datetime, timezone


BASE_URL = 'https://petstore.swagger.io/v2'
fake = Faker()

@pytest.fixture(scope='session')
def base_url():
    return BASE_URL

@pytest.fixture
def file_path():
    current_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(current_dir, ".."))
    path = os.path.join(project_root, "img", "cat.png")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл не найден: {path}")
    return path

@pytest.fixture(scope='session')
def pet_api(base_url):
    return PetAPI(base_url)

@pytest.fixture()
def create_pet(pet_api, pet_data):
    response_add_pet = pet_api.add_pet(pet_data)
    yield response_add_pet
    pet_api.delete_pet(pet_data['id'])

@pytest.fixture(scope="session")
def store_api(base_url):
    return StoreAPI(base_url)

@pytest.fixture()
def create_order(store_api, store_order_data):
    response_order = store_api.new_order(store_order_data)
    yield response_order

# @pytest.fixture(scope="session")
# def user_api(base_url):
#     return UserAPI(base_url)
#
#



@pytest.fixture
def pet_data():
    return {
        'id': fake.random_int(min=100000, max=999999),
        'name': fake.first_name(),
        'status': fake.random_element(['available', 'pending', 'sold'])
    }

@pytest.fixture
def new_pet_data():
    return {
        'name': fake.first_name(),
        'status': fake.random_element(['available', 'pending', 'sold'])
    }

@pytest.fixture
def store_order_data():
    now_utc = datetime.now(timezone.utc)
    return {
      "id": fake.random_int(min=1, max=10),
      "petId": fake.random_int(min=100000, max=999999),
      "quantity": fake.random_int(min=1, max=1000),
      "shipDate": now_utc.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
      "status": fake.random_element(['sold', 'string', 'available', 'pending']),
      "complete": fake.random_element(['true', 'false'])
    }

@pytest.fixture
def user_data():
    username = fake.user_name()
    return {
        "id": fake.random_int(min=10000, max=99999),
        "username": username,
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": "Test123!",
        "phone": fake.phone_number(),
        "userStatus": 1,
    }
