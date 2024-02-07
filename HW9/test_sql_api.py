from bd import BD
from employee import API
import pytest

api = API("https://x-clients-be.onrender.com")
db = BD("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")

name = "Skyeng"
descr = "test"
company = api.create_company(name, descr)
new_id = company["id"]

def setup_module(module):
    db.create_table()

def teardown_module(module):
    db.db.dispose()

def test_create_and_get_employee():

    db.insert_employee("Mikki", "Maus", "+123456789", new_id)
    employee_list = api.get_list_employee(new_id)
    assert any(employee["firstName"] == "Mikki" and employee["lastName"] == "Maus" for employee in employee_list)


def test_update_employee():

    db.insert_employee("Mikki", "Maus", "+123456789", new_id)
    employees = db.get_employees()

    employee_id = employees[0]["id"]
    db.update_employee(employee_id, "Mikki", "Mos", "Middle", "+987654321", "mikki.mos@example.com", "http://example.com")

    updated_employee = db.get_employees()[0]
    assert updated_employee["first_name"] == "Mikki"
    assert updated_employee["last_name"] == "Mos"
    assert updated_employee["phone"] == "+987654321"

def test_delete_employee():
    db.insert_employee("Mikki", "Mos", "+123456789", new_id)
    len_before = len(db.get_employees())
    employees = db.get_employees()
    employee_id = employees[0]["id"]
    db.delete_employee(employee_id)

    len_after = len(db.get_employees())

    assert len_before - len_after == 1