import pytest
from employee import API
from bd import BD

# Подключение к БД
db_string = 'postgresql://x_clients_user:axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com/x_clients'
bd_instance = BD(db_string)

# Подключение к API
creds = {'username': 'raphael', 'password': 'cool-but-crude'}
base_url = 'https://x-clients-be.onrender.com'
api_instance = API(base_url)

# Body employee API
body_new_employee = {
    "id": 0,
    "firstName": "Valentina",
    "lastName": "Balashova",
    "middleName": "Alexsandrovna",
    "companyId": None,
    "email": "ftyftjwvf@mai.ru",
    "url": "www",
    "phone": "+123456789",
    "birthdate": "2024-01-11T07:45:04.659Z",
    "isActive": True
}

# Body update API
body_for_patch = {
    "lastName": "Dolgopolova",
    "email": "lentina86@mail.ru",
    "url": "www",
    "phone": "+123456789",
    "isActive": True
}

# Получение id компании через API
headers = api_instance.get_headers(creds)
response = api_instance.get_company()
company_id = response.json()[0]['id']

body_db_new_employee = [{"first_name":"Valentina", "last_name":"Balashova", "middle_name":"Alexsandrovna", "phone":"+79193369589", \
        "email":"lentina86@mail.ru", "birthdate":"2024-01-11T07:45:04.659Z", "avatar_url":"www", "company_id" : company_id}
        ]
db_email_employee = 'ftyftjwvf@mai.ru'

@pytest.fixture(scope="module")
def setup_db():
    # Подготовка БД и получение id компании
    company_id = bd_instance.insert_company("TestCompany")
    yield company_id
    bd_instance.delete_company(company_id)

def test_create_and_get_employee(setup_db):
    company_id = setup_db
    len_before = len(bd_instance.get_employees())

    bd_instance.insert_employee("Валентина", "Балашова", "+123456789", company_id)

    len_after = len(bd_instance.get_employees())

    assert len_after - len_before == 1

    employee_list = api_instance.get_employee(headers, company_id)
    assert any(employee["firstName"] == "Валентина" and employee["lastName"] == "Балашова" for employee in employee_list.json())

def test_update_employee(setup_db):
    company_id = setup_db
    bd_instance.insert_employee("Jane", "Doe", "+123456789", company_id)

    employees = bd_instance.get_employees()
    assert len(employees) > 0

    employee_id = employees[0]["id"]
    bd_instance.update_employee(employee_id, "Jane", "Doe", "+123456789", company_id)

    updated_employee = bd_instance.get_employee_by_id(employee_id)
    assert updated_employee["last_name"] == "Doe"

def test_delete_employee(setup_db):
    company_id = setup_db
    bd_instance.insert_employee("John", "Doe", "+123456789", company_id)

    len_before = len(bd_instance.get_employees())

    employees = bd_instance.get_employees()
    employee_id = employees[0]["id"]
    bd_instance.delete_employee(employee_id)

    len_after = len(bd_instance.get_employees())

    assert len_before - len_after == 1