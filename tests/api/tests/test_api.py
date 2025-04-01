import requests
import pytest
import allure
from tests.api.canftest import db_connection, valid_user
from tests.api.endpoints import CreatePage
from tests.api.endpoints import TaskPage
from tests.api.endpoints import GetTask
from tests.api.payload.payload import valid_create_payload, valid_new_task, valid_update_task, valid_new_create_payload, \
    new_task


@allure.feature('Login page')
@allure.story("Аутентификация нового пользователя")
@allure.severity(allure.severity_level.NORMAL)
def test_new_user(valid_user):
    with allure.step("Создание нового пользователя"):
        new_user = CreatePage()
        new_user.new_user(valid_new_create_payload)
        new_user.check_response_is_201()


@allure.feature('Login page')
@allure.story("Аутентификация существующего пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_user():
    session = requests.Session()
    with allure.step("Аутентификация существующего пользователя"):
        new_user = CreatePage()
        new_user.login_user(valid_create_payload, session)
        new_user.check_response_is_200()


@allure.feature('Task page')
@allure.story("Создание задачи")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_task():
    session = requests.Session()
    with allure.step("Аутентификация пользователя"):
        creat_user = CreatePage()
        creat_user.login_user(valid_create_payload, session)
        assert creat_user.response.status_code == 200, f"Ошибка: {creat_user.response_json}"
    with allure.step("Создание пустой задачи"):
        new_create_task = TaskPage()
        new_create_task.new_task(new_task, session)
        new_create_task.check_response_is_201(), "Создалась пустая задача"


@allure.feature('Task page')
@allure.story("Работа с задачами")
@allure.severity(allure.severity_level.CRITICAL)
def test_task(db_connection):
    session = requests.Session()
    with allure.step("Аутентификация пользователя"):
        creat_user = CreatePage()
        creat_user.login_user(valid_create_payload, session)
        assert creat_user.response.status_code == 200, f"Ошибка: {creat_user.response_json}"
    with allure.step("Создание новой задачи"):
        cread_task = TaskPage()
        cread_task.new_task(valid_new_task, session)
        cread_task.check_response_is_201(), 'Задача не создана'
    with allure.step("Получение задачи по ID"):
        task_id = cread_task.get_task_id()
    with allure.step("Поиск задачи в базе данных"):
        cur = db_connection.cursor()
        cur.execute('SELECT * FROM task WHERE id = %s', (task_id,))
        task = cur.fetchone()
        cur.close()
        assert task is not None, f"Задача с ID {task_id} не найдена в базе данных"
    with allure.step("Обновление задачи"):
        crud_update_task = TaskPage()
        crud_update_task.update_task(task_id, valid_update_task, session)
        crud_update_task.check_response_is_200(), 'Задача не обновлена'
    with allure.step("Обновление статуса задачи"):
        crud_update_task.update_status_task(task_id, session)
        crud_update_task.check_response_is_200(), 'Статуст задачи не обновлен'
    with allure.step("Удаление задачи"):
        crud_delete_task = TaskPage()
        crud_delete_task.delete_task(task_id, session)
        crud_delete_task.check_response_is_204(), 'Задача не удалена'


@allure.feature('Task page')
@allure.story("РАбота с задачами")
def test_get_task():
    session = requests.Session()
    with allure.step("Аутентификация пользователя"):
        create_user = CreatePage()
        create_user.login_user(valid_create_payload, session)
    with allure.step("Получение списка всех задач"):
        all_tasks = GetTask()
        all_tasks.get_task(session)
        all_tasks.check_response_is_200(), 'Задачи не найдены'
