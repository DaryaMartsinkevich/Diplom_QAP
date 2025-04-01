import allure
import pytest

from tests.ui.pages import EditPage
from tests.ui.pages import CreateTaskPage
from tests.ui.conftest import driver_login
from tests.ui.pages import LoginPage
from tests.ui.pages import RegisterPage
from tests.ui.pages import TaskPage


@pytest.mark.parametrize(
    "username, password",
    [
        ('Hena', '123456789'),
        ("Dima", "987654321"),
        ("Aniya", 'hanna'),
        (" ", 'password1'),
        ('User1', ' '),
        (' ', ' ')
    ]
)
@allure.feature("Тест пользователя")
@allure.story("Регистрация нового пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_register_user(driver, db_connection, username, password):
    with allure.step("Входим на страницу регистирации нового пользователя"):
        register_user = RegisterPage(driver)
        register_user.get_register_page()
        assert 'register' in driver.current_url, "Не произошел переход на страницк регистрации"

    with allure.step("Регистирируем нового пользователя"):
        register_user.enter_username(username)
        register_user.enter_password(password)
        register_user.click_register()

    with allure.step("Проверяем валидность данных"):
        if username == ' ':
            assert register_user.get_error_message(), "Имя пользователя обязательно"
        elif password == ' ':
            assert register_user.get_error_message(), "Пароль обязателен"
        elif username == ' ' and password == ' ':
            assert register_user.get_error_message(), "Имя пользователя обязательно"
            assert register_user.get_error_message(), "Пароль обязателен"
        elif len(password) < 6:
            assert register_user.get_error_message(), "Пароль должен содержать не менее 6 символов"


@pytest.mark.parametrize(
    "username, password",
    [
        ('Darya', 'red2665642')
    ]
)
@allure.feature("Тест пользователя")
@allure.story("Авторизация существующего пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_autorization_user(driver, username, password):
    with allure.step("Входим на страницу аворизации"):
        login_user = LoginPage(driver)
        login_user.get_login_page()
        assert 'login' in driver.current_url, "Не произошел переход на страницу авторизации"
    with allure.step("Вводим данные для авторизации"):
        login_user.enter_username(username)
        login_user.enter_password(password)
        login_user.click_login()
    with allure.step("Переходим на страницу с задачами"):
        task_page = TaskPage(driver)
        assert 'task' in driver.current_url, "Не произошел переход на страницу задач"
    with allure.step("Выход из системы"):
        task_page.logout()
        assert 'login' in driver.current_url, "Не произошел переход на страницу авторизации"
        login_message = login_user.get_message()
        log_message = "Вы вышли из системы"
        assert login_message == log_message, (
            f"Полученное сообщение: {login_message} != {log_message}")


@allure.feature("Тест задач")
@allure.story("Работа с задачами")
@allure.severity(allure.severity_level.CRITICAL)
def test_task(driver_login):
    with allure.step("Авторизация пользователя"):
        task_page = TaskPage(driver_login)
        assert 'task' in driver_login.current_url, 'Авторизация не выполнена'
    with allure.step("Переход на страницу с задачами"):
        task_page.creat_task()
        create_task = CreateTaskPage(driver_login)
        assert 'create' in driver_login.current_url, 'Страница с задачами не открыта'
    with allure.step("Создание задачи"):
        create_task.enter_title('Написать диплом')
        create_task.enter_description('СЕЙЧАС')
        create_task.click_submit_button()
        create_task_message = task_page.get_success_message()
        successe_message = 'Задача успешно создана'
        assert create_task_message == successe_message, (
            f"Полученное сообщение: {create_task_message} != {successe_message}")
    with allure.step('Редактирование задачи'):
        task_page.edit_task()
        edit_task = EditPage(driver_login)
        edit_task.clear_title()
        edit_task.edit_title("Написать отличный диплом")
        edit_task.clear_description()
        edit_task.edit_description('СЕЙЧАС, ДАША!')
        edit_task.click_submit_button()
    with allure.step("Проверим сообщение об успешном редактировании"):
        task_message = task_page.get_success_message()
        update_task = "Задача успешно обновлена"
        assert task_message == update_task, (
            f"Полученное сообщение: {task_message} != {update_task}")
    with allure.step("Изменим статус задачи"):
        task_page.edit_task()
        edit_task.edit_status()
        edit_task.click_submit_button()


@allure.feature("Тест задач")
@allure.story("Удаление задачи")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_task(driver_login):
    with allure.step("Авторизация пользователя"):
        task_page = TaskPage(driver_login)
        assert 'task' in driver_login.current_url, 'Авторизация не выполнена'
    with allure.step("Переход на страницу с задачами"):
        task_page.creat_task()
        create_task = CreateTaskPage(driver_login)
        assert 'create' in driver_login.current_url, 'Страница с задачами не открыта'
    with allure.step("Создание задачи"):
        create_task.enter_title('Написать диплом')
        create_task.enter_description('СЕЙЧАС')
        create_task.click_submit_button()
        create_task_message = task_page.get_success_message()
        successe_message = 'Задача успешно создана'
        assert create_task_message == successe_message, (
            f"Полученное сообщение: {create_task_message} != {successe_message}")
    with allure.step("Удаление задачи"):
        task_page.delete_task()
        task_page.delete_button_confirm()
        delete_message = task_page.get_success_message()
        message_delete = 'Задача успешно удалена'
        assert delete_message == message_delete, (
            f"Полученное сообщение: {delete_message} != {message_delete}")

