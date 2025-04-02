import jsonschema
import requests
from tests.api.endpoints.base_endpoint import Endpoint
from tests.api.payload.payload import headers


class GetTask(Endpoint):
    schema = {
        "id": 0,
        "title": "string",
        "description": "string",
        "created_at": "2025-03-19T14:39:08.809Z",
        "completed": True,
        "user_id": 0
    }

    def get_task(self, session):
        self.response = session.get(f"{self.url}/tasks")
        self.response_json = self.response.json()


