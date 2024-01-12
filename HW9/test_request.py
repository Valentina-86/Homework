import requests
from employee import Employee

def test_employee():

    test_employee = Employee('https://x-clients-be.onrender.com')
    test_employee.creds('raphael', 'cool-but-crude')
    test_employee.authorize()
    test_employee.get_headers()
    test_employee.simple_reg()
    test_employee.create_employee()
    test_employee.new_employee(0, "Valentina", "Balashova", "Alexsandrovna", "lentina86@mail.ru", "www", \
                               "+79193369589", "2024-01-11T07:45:04.659Z", True)
    test_employee.employee()
    test_employee.update_employee("Dolgopolova", "lentina86@mail.ru", "www", "+79193369589", True)

    assert test_employee.my_headers == 'token'
    assert test_employee.company == id
    assert test_employee.get_employee is not None
    assert test_employee.new == id
    assert test_employee.spisok == id
    assert test_employee.resp == id