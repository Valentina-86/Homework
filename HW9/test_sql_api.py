from bd import BD
from employee import API
import pytest

api = API("https://x-clients-be.onrender.com")
db = BD ("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")



def setup_module(module):
    db.create_table()



def test_create_and_get_employee():
    name = "SkyPro"
    descr = "testing"
    company = api.create_company(name, descr)
    new_company_id = company["id"]
    len_before = len(db.get_employees())


    db.insert_employee("Mikki", "Maus", "+123456789", new_company_id)
    len_after = len(db.get_employees())
    assert len_after - len_before == 1
    employee_list = api.get_list_employee(new_company_id)
    assert any(employee["firstName"] == "Mikki" and employee["lastName"] == "Maus" for employee in employee_list)


def test_update_employee():

    employees = db.get_employees()
    assert len(employees) == 0

    employee_id = employees[0]["id"]
    db.update_employee(employee_id, "Mikki", "Mos", "Middle", "+66666666", "mikki.mos@example.com", "http://test.com")

    updated_employee = db.get_employees()[0]
    assert updated_employee["first_name"] == "Mikki"
    assert updated_employee["last_name"] == "Mos"
    assert updated_employee["middle_name"] == "Middle"
    assert updated_employee["phone"] == "+66666666"
    assert updated_employee["email"] == "mikki.mos@example.com"
    assert updated_employee["avatar_url"] == "http://test.com"

def test_delete_employee():

    employees = db.get_employees()
    
    employee_id = employees[0]["id"]
    db.delete_employee(employee_id)

    deleted_employee = db.get_employee_by_id(employee_id)
    assert deleted_employee is None