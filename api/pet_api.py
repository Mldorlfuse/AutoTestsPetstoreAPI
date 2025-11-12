from .base_api import BaseAPI

class PetAPI(BaseAPI):

    def add_pet(self, pet_data):
        body = {
                  "id": pet_data["id"],
                  "category": {
                    "id": 0,
                    "name": "string"
                  },
                  "name": pet_data["name"],
                  "photoUrls": [
                    "string"
                  ],
                  "tags": [
                    {
                      "id": 0,
                      "name": "string"
                    }
                  ],
                  "status": pet_data["status"][0]
                }
        return self.post("/pet", json=pet_data)

    def get_pet(self, pet_id):
        return self.get(f"/pet/{pet_id}")

    def update_pet(self, pet_data):
        return self.put("/pet", json=pet_data)

    def delete_pet(self, pet_id):
        return self.delete(f"/pet/{pet_id}")