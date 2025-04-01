import pytest
import os
import psycopg2
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from tests.ui.pages import RegisterPage, LoginPage
from tests.ui.settings import DB_CONFIG


@pytest.fixture
def db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    yield conn
    cur = conn.cursor()
    sql_delete = 'DELETE FROM "task"'
    cur.execute(sql_delete)
    sql_delete = """DELETE FROM "user" WHERE username != 'Darya'"""
    cur.execute(sql_delete)
    # Фиксируем изменения
    conn.commit()

    # Узнаем, сколько строк было удалено
    rows_deleted = cur.rowcount
    print(f"Удалено строк: {rows_deleted}")
    conn.close()
    print("Соединение с БД закрыто.")


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")

    # Используем WebDriver Manager для автоматической установки ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def driver_login(driver, db_connection):
    register = RegisterPage(driver)
    username, password = ('Darya', 'red2665642')
    if register.user_not_exists(db_connection, username):
        register.get_register_page()
        register.valid_user(username, password)
    login = LoginPage(driver)
    login.valid_user(username, password)
    return driver


