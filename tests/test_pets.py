def test_pet_crud(pet_api, pet_data):
    response = pet_api.add_pet(pet_data)
    print(response.json())
    response2 = pet_api.get_pet(response.json()['id'])
    print(response2.json())