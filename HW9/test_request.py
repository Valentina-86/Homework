from employee import Employee

creds = {'username': 'raphael', 'password': 'cool-but-crude'}
base_url = 'https://x-clients-be.onrender.com'
body_new_employee = {
    "id": 0,
    "firstName": "Valentina",
    "lastName": "Balashova",
    "middleName": "Alexsandrovna",
    "companyId": None,
    "email": "lentina86@mail.ru",
    "url": "www",
    "phone": "+79193369589",
    "birthdate": "2024-01-11T07:45:04.659Z",
    "isActive": True
}
body_for_patch = {
    "lastName": "Dolgopolova",
    "email": "lentina86@mail.ru",
    "url": "www",
    "phone": "+79193369589",
    "isActive": True
}


def tests():
    test_employee = Employee(base_url)
    headers = test_employee.get_headers(creds)
    assert headers is not None

    response = test_employee.get_company()
    body_new_employee['companyId'] = response.json()[0]['id']
    assert response.status_code == 200

    response = test_employee.authorize(creds)
    assert response.status_code == 201

    response = test_employee.get_employee(headers, body_new_employee['companyId'])
    assert response.status_code == 200

    response = test_employee.new_employee(creds, body_new_employee, headers)
    id_ = response.json()['id']
    assert response.status_code == 201

    response = test_employee.get_employee_by_id(id_, headers)
    assert response.status_code == 200
    assert response.json().get('lastName') == 'Balashova'

    response = test_employee.update_employee(id_, body_for_patch, headers)
    assert response.status_code == 200
    assert response.json().get('id') == id_
