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

    @staticmethod
    def user_not_exists(conn, username):
        cur = conn.cursor()
        cur.execute(
            'SELECT COUNT(*) from "user" WHERE username =%s', (username,)
        )
        return cur.fetchone()[0] == 0

    def login_user(self, payload, session):
        self.response = session.post(f"{self.url}/login", json=payload)
        self.response_json = self.response.json()
        return session


