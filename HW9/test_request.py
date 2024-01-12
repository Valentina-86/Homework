import requests

base_url = 'https://x-clients-be.onrender.com'
creds = {'username' : 'raphael','password' : 'cool-but-crude'}
my_company = {'company' : 3687}
id_employee = {'id' : 1719}


def get_headers() -> dict:
    #функция возвращающая headers
    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["userToken"]
    
    my_headers= {}
    my_headers["x-client-token"] = token

    return my_headers

    assert my_headers is not None

def test_simple_reg():
    company = requests.get(base_url+'/company')

    assert company.status_code == 200
    assert company is not None
    
def test_auth():
    #авторизация
    auth = requests.post(base_url+'/auth/login', json=creds)

    assert auth.status_code == 201

def test_create_employee():
    #получение списка пользователей
    get_employee = requests.get(f'{base_url}/employee/{my_company['company']}', headers=get_headers())

    assert get_employee.status_code == 200
    assert my_company is not None

def test_new_employee():
    #тело запроса
    body = {
        "id": 0,
        "firstName": "Valentina",
        "lastName": "Balashova",
        "middleName": "Alexsandrovna",
        "companyId": my_company['company'],
        "email": "lentina86@mail.ru",
        "url": "www",
        "phone": "+79193369589",
        "birthdate": "2024-01-11T07:45:04.659Z",
        "isActive": True
    }

    #создание нового пользователя
    new_employee = requests.post(base_url+'/employee', json=body, headers=get_headers())
    return new_employee.json()["id"]

    assert resp.status_code == 201
    assert body is not None
    assert get_headers is not None



def test_employee():
    #получить сотрудника по id
    employee = requests.get(f'{base_url}/employee/{id_employee['id']}', headers=get_headers())

    assert employee.status_code == 200
    assert id_employee is not None

def test_update_employee():
    #тело запроса
    body = {
        "lastName": "Dolgopolova",
        "email": "lentina86@mail.ru",
        "url": "www",
        "phone": "+79193369589",
        "isActive": True
    }
    
    #изменить информацию о сотруднике
    resp = requests.patch(f'{base_url}/employee/{id_employee['id']}',json=body, headers=get_headers())

    assert resp.status_code == 200
    assert body is not None
    assert get_headers is not None
    assert id_employee is not None