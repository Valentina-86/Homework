import requests

class API:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_headers(self, creds) -> dict:
        # функция возвращающая headers
        resp = requests.post(self.base_url + '/auth/login', json=creds)
        token = resp.json()["userToken"]
        my_headers = {"x-client-token": token}
        return my_headers

    def get_company(self):
        resp = requests.get(self.base_url + '/company')
        return resp

    def authorize(self, creds):
        # авторизация
        resp = requests.post(self.base_url + '/auth/login', json=creds)
        return resp

    def get_employee(self, headers, id_):
        # получение списка пользователей
        resp = requests.get(f'{self.base_url}/employee/{id_}', headers=headers)
        return resp

    def new_employee(self, creds, body, headers):
        # создание нового пользователя
        resp = requests.post(self.base_url + '/employee', json=body, headers=headers)
        return resp

    def get_employee_by_id(self, id_, headers):
        # получить сотрудника по id
        resp = requests.get(f'{self.base_url}/employee/{id_}', headers=headers)
        return resp

    def update_employee(self, id_, body, headers):
        # изменить информацию о сотруднике
        resp = requests.patch(f'{self.base_url}/employee/{id_}', json=body, headers=headers)
        return resp