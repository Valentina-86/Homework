import allure
from table import TableBd
from api import API


employee_id = None
api = API("https://x-clients-be.onrender.com")
db = TableBd("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")



def setup_module(module):
    db.create_table()

@allure.story('Добавление пользователя')
@allure.feature('CREATE')
@allure.title('Добавление нового пользователя')
@allure.description('Добавление пользователя при помощи id компании')
@allure.severity('BLOCKER')
@allure.epic('Пользователи')
def test_create_and_get_employee():
    global employee_id
    with allure.step('Ввести name и descr'):
        name = "SkyPro"
        descr = "testing"

    with allure.step('Получить id компании'):
        company = api.create_company(name, descr)
        new_company_id = company["id"]
        len_before = len(db.get_employees())

    with allure.step('Добавить нового пользователя'):
        employee_id = db.insert_employee("Mikki", "Maus", "+123456789", new_company_id)
        len_after = len(db.get_employees())

    with allure.step('Проверить что пользователь добавился'):
        assert len_after - len_before == 1
        employee_list = api.get_list_employee(new_company_id)

    with allure.step('Проверить актуальность заполненных данных'):
        assert any(employee["firstName"] == "Mikki" and employee["lastName"] == "Maus" for employee in employee_list)

@allure.story('Редактирование пользователя')
@allure.feature('UPDATE')
@allure.title('Редактирование пользователя по id')
@allure.description('Редактирование пользователя при помощи id пользователя')
@allure.severity('BLOCKER')
@allure.epic('Пользователи')
def test_update_employee():
    global employee_id
    with allure.step('Отредактировать пользователя'):
        db.update_employee(employee_id, "Jhon", "Connor", "Middle", "+66666666", "mikki.mos@example.com", "http://test.com")

    with allure.step('Проверить что отредактированные поля изменились'):
        updated_employee = db.get_employees()[-1]
        assert updated_employee["first_name"] == "Jhon"
        assert updated_employee["last_name"] == "Connor"
        assert updated_employee["middle_name"] == "Middle"
        assert updated_employee["phone"] == "+66666666"
        assert updated_employee["email"] == "mikki.mos@example.com"
        assert updated_employee["avatar_url"] == "http://test.com"

@allure.story('Удаление пользователя')
@allure.feature('DELETE')
@allure.title('Удаление пользователя по id')
@allure.description('Удаление пользователя при помощи id пользователя')
@allure.severity('BLOCKER')
@allure.epic('Пользователи')
def test_delete_employee():
    employees = db.get_employees()

    with allure.step('Удалить пользователя по id'):
        employee_id = employees[-1]["id"]
        db.delete_employee(employee_id)

    with allure.step('Проверить, что пользователь удалился'):
        deleted_employee = db.get_employee_by_id(employee_id)
        assert deleted_employee is None