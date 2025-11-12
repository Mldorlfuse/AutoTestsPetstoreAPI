import pytest
from faker import Faker
from api.pet_api import PetAPI
# from api.user_api import UserAPI
# from api.store_api import StoreAPI

BASE_URL = "https://petstore.swagger.io/v2"
fake = Faker()


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def pet_api(base_url):
    return PetAPI(base_url)


# @pytest.fixture(scope="session")
# def user_api(base_url):
#     return UserAPI(base_url)
#
#
# @pytest.fixture(scope="session")
# def store_api(base_url):
#     return StoreAPI(base_url)


@pytest.fixture
def pet_data():
    return {
        "id": fake.random_int(min=100000, max=999999),
        "name": fake.first_name(),
        "status": fake.random_element(["available", "pending", "sold"]),
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
