import pytest
import requests
import psycopg2

from tests.api.endpoints import CreatePage
from tests.api.payload.payload import valid_create_payload, valid_new_create_payload
import os


DB_CONFIG = {
    'dbname': os.environ.get('POSTGRES_DB', 'taskmanager'),
    'user': os.environ.get('POSTGRES_USER', 'postgres'),
    'password': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
    'host': os.environ.get('POSTGRES_HOST', 'localhost'),
    'port': os.environ.get('POSTGRES_PORT', '5432')
}


@pytest.fixture
def db_connection():
    print("🔌 Подключение к БД...")
    conn = psycopg2.connect(**DB_CONFIG)
    yield conn
    conn.close()
    print("🔌 Соединение с БД закрыто.")


@pytest.fixture
def valid_user():
    session = requests.Session()
    user = CreatePage()
    user.login_user(valid_create_payload, session)
    user.check_response_is_200()
    return user, session
