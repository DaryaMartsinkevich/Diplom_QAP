import requests
import jsonschema
from tests.api.endpoints import Endpoint


class CreatePage(Endpoint):
    schema = {
        "username": "string",
        "password": "string"
    }

    def new_user(self, payload):
        self.response = requests.post(f"{self.url}/register", json=payload)
        self.response_json = self.response.json()

    def login_user(self, payload, session):
        self.response = session.post(f"{self.url}/login", json=payload)
        self.response_json = self.response.json()
        return session


