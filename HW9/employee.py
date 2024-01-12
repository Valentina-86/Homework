import requests

class Employee:

    def __init__(self, base_url):
        self.base_url = base_url

    def creds(self, name, password):
        return {self.username : name, self.password : password}

    def authorize(self):
        #авторизация
        self.auth = requests.post(self.base_url+'/auth/login', json=self.creds())

    def get_headers(self) -> dict:
        #функция возвращающая headers
        self.resp = requests.post(self.base_url+'/auth/login', json=self.creds())
        token = self.resp.json()["userToken"]
        
        self.my_headers= {}
        self.my_headers["x-client-token"] = token

        return self.my_headers

    def simple_reg(self):
        self.company = requests.get(self.base_url+'/company').id
        return self.company['id']

    def create_employee(self):
        #получение списка пользователей
        self.get_employee = requests.get(f'{self.base_url}/employee/{self.simple_reg()}', headers=self.get_headers())
        return self.get_employee

    def new_employee(self, id, firstName, lastName, middleName, email, url, phone, birthdate, isActive):
        body = {
        "id": id,
        "firstName": firstName,
        "lastName": lastName,
        "middleName": middleName,
        "companyId": self.simple_reg(),
        "email": email,
        "url": url,
        "phone": phone,
        "birthdate": birthdate,
        "isActive": isActive
        }

        #создание нового пользователя
        self.new = requests.post(self.base_url+'/employee', json=body, headers=self.get_headers()).id
        return self.new

    def employee(self):
        #получить сотрудника по id
        self.spisok = requests.get(f'{self.base_url}/employee/{self.new_employee}', headers=self.get_headers())
        return self.spisok

    def update_employee(self, lastName, email, url, phone, isActive):
        body = {
        "lastName": lastName,
        "email": email,
        "url": url,
        "phone": phone,
        "isActive": isActive
    }
        
        #изменить информацию о сотруднике
        self.resp = requests.patch(f'{self.base_url}/employee/{self.new_employee}',json=body, headers=self.get_headers())
        return self.resp
