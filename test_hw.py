import requests
import json

base_url = 'https://x-clients-be.onrender.com'

def authorize():
    creds = {
        'username' : 'raphael',
        'password' : 'cool-but-crude'
    }
    return creds.json()

def test_company():
    
    resp = requests.get(base_url+'/company')
    response_body = resp.json()

    assert resp.status_code == 200
    
def test_auth():
    
    resp = requests.post(base_url+'/auth/login', json=authorize())
    token = resp.json()["userToken"]
    assert resp.status_code == 201

def test_create_employee():

    creds = {
        'username' : 'raphael',
        'password' : 'cool-but-crude'
    }
    my_company = {
      'company' : '3687'
    }

    #авторизация
    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["userToken"]

    my_headers= {}
    my_headers["x-client-token"] = token
    
    #получение списка пользователей
    resp = requests.get(f'{base_url}/employee/{my_company['company']}', headers=my_headers)
    assert resp.status_code == 200

def test_new_employee():

    creds = {
        'username' : 'raphael',
        'password' : 'cool-but-crude'
    } 
    #авторизация
    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["userToken"]
    #получение токена
    my_headers= {}
    my_headers["x-client-token"] = token
    #компания
    my_company = {
      'company' : 3687
    }
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

    #создание пользователя
    resp = requests.post(base_url+'/employee', json=body, headers=my_headers)
    assert resp.status_code == 201

def test_employee():

    creds = {
        'username' : 'raphael',
        'password' : 'cool-but-crude'
    } 
    #авторизация
    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["userToken"]
    #получение токена
    my_headers= {}
    my_headers["x-client-token"] = token
    #сотрудник
    id_employee = {
        'id' : 1719
    }

    #получить сотрудника по id
    resp = requests.get(f'{base_url}/employee/{id_employee['id']}', headers=my_headers)
    assert resp.status_code == 200

def test_update_employee():

    creds = {
        'username' : 'raphael',
        'password' : 'cool-but-crude'
    } 
    #авторизация
    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["userToken"]
    #получение токена
    my_headers= {}
    my_headers["x-client-token"] = token
    #сотрудник
    id_employee = {
        'id' : 1719
    }
        #тело запроса
    body = {
        "lastName": "Dolgopolova",
        "email": "lentina86@mail.ru",
        "url": "www",
        "phone": "+79193369589",
        "isActive": True
    }
    
    #изменить информацию о сотруднике
    resp = requests.patch(f'{base_url}/employee/{id_employee['id']}',json=body, headers=my_headers)
    assert resp.status_code == 200