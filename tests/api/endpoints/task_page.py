import requests
from tests.api.endpoints.base_endpoint import Endpoint
from tests.api.payload.payload import headers


class TaskPage(Endpoint):
    schema = {
        "title": "string",
        "description": "string",
        "completed": True
    }

    def new_task(self, payload, session):
        self.response = session.post(f'{self.url}/tasks', json=payload, headers=headers)
        self.response_json = self.response.json()

    def get_task_id(self):
        task_id = self.get_data()
        return task_id['id']

    def get_task_title(self):
        return self.get_data()['title']

    def get_task_description(self):
        return self.get_data()['description']

    def get_task_status(self):
        return self.get_data()['completed']

    def update_task(self, task_id, payload, session):
        self.response = session.put(f"{self.url}/tasks/{task_id}", json=payload, headers=headers)
        self.response_json = self.response.json()

    def update_status_task(self, task_id, session):
        self.response = session.post(f"{self.url}/tasks/{task_id}/toggle")
        self.response_json = self.response.json()

    def delete_task(self, task_id, session):
        self.response = session.delete(f"{self.url}/tasks/{task_id}")
