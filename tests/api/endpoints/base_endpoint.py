import jsonschema
import requests
from tests.api import settings as settings

default_session = requests.Session()


class Endpoint:
    response = None
    response_json = None
    schema = {}
    session = default_session
    url = settings.BASE_URL

    def check_response_is_200(self):
        assert self.response.status_code == 200, \
            f'Ожидаем статус-код 200, но получен {self.response.status_code}'

    def check_response_is_201(self):
        assert self.response.status_code == 201, \
            f'Ожидаем статус-код 201, но получен{self.response.status_code}'

    def check_response_is_204(self):
        assert self.response.status_code == 204, \
            f'Ожидаем статус-код 204, но получен{self.response.status_code}'

    def check_response_is_400(self):
        assert self.response.status_code == 400, \
            f'Ожидаем статус-код 400, но получен{self.response.status_code}'

    def check_response_is_401(self):
        assert self.response.status_code == 401, \
            f'Ожидаем статус-код 401, но получен{self.response.status_code}'

    def validate(self, data):
        jsonschema.validate(instance=data, schema=self.schema)

    def check_response_is_404(self):
        assert self.response.status_code == 404, \
            f'Ожидаем статус-код 404, но получен{self.response.status_code}'

    def get_data(self):
        return self.response.json()
