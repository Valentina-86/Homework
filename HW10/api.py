import requests


class API:

    def __init__(self, url):
        self.url = url

    def get_token(self, user='raphael', password='cool-but-crude') -> str:
        """
        Аутентифицирует пользователя и возвращает токен пользователя.

        params:
        user (str, optional): Имя пользователя для аутентификации. По умолчанию 'raphael'.
        password (str, optional): Пароль пользователя для аутентификации. По умолчанию 'cool-but-crude'.

        """
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(f"{self.url}/auth/login", json=creds)
        return resp.json()["userToken"]

    def create_company(self, name, description='') -> dict:
        """
        Создает новую компанию с заданными именем и описанием.

        Эта функция отправляет POST-запрос на сервер с данными компании в формате JSON.
        Заголовок запроса включает токен клиента, полученный с помощью метода self.get_token().

        Параметры:
        name (str): Имя компании.
        description (str, optional): Описание компании. По умолчанию пустая строка.

        Возвращает:
        dict: Ответ сервера в формате JSON.

        Исключения:
        requests.exceptions.RequestException: Если запрос не удался по какой-либо причине.
        """
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(f"{self.url}/company", json=company, headers=my_headers)
        return resp.json()

    def get_list_employee(self, id:int) -> list:
        """
        Получает список сотрудников компании по её идентификатору.

        Исключения:
        requests.exceptions.RequestException: Если запрос не удался по какой-либо причине.
        """
        my_params = {
            "company": id
        }
        resp = requests.get(f"{self.url}/employee", params=my_params)
        return resp.json()

    def get_employee_by_id(self, id_employee:int) -> dict:
        """
        Получает информацию о сотруднике по его уникальному идентификатору.

        Исключения:
        requests.exceptions.RequestException: Если запрос не удался по какой-либо причине.
        """
        resp = requests.get(f"{self.url}/employee/{id_employee}")
        return resp.json()

    def add_new_employee(self, new_id:int, first_name:str, last_name:str) -> dict:
        """
        Добавляет нового сотрудника в систему с заданными параметрами.

        Исключения:
        requests.exceptions.RequestException: Если запрос не удался по какой-либо причине.
        """
        employee = {
            "id": 1,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": "-",
            "companyId": new_id,
            "email": "test@test.com",
            "url": "string",
            "phone": "89999999999",
            "birthdate": "2023-12-25T18:54:13.783Z",
            "isActive": 'true'
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(f"{self.url}/employee", headers=my_headers, json=employee)
        return resp.json()

    def update_employee_info(self, id_employee:int, last_name:str, email:str) -> dict:
        """
        Обновляет информацию о сотруднике в системе.
        """
        user_info = {
            "lastName": last_name,
            "email": email,
            "isActive": True
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(f"{self.url}/employee/{id_employee}", headers=my_headers, json=user_info)
        return resp.json()