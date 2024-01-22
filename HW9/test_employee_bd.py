from sqlalchemy import create_engine, MetaData
import sqlalchemy

db_string = 'postgresql://x_clients_user:axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com/x_clients'
engine = create_engine(db_string)

connection = engine.connect()
metadata = MetaData()
metadata.bind = engine
metadata.reflect(engine)

tables = metadata.tables.keys()

# Забрать таблицу employee из БД 
employee = metadata.tables['employee']

# Забрать таблицу company из БД
company_table = metadata.tables['company']
# Получить id компании из таблицы company
select_all_query = sqlalchemy.select(company_table)
result = connection.execute(select_all_query)
company_id = result.fetchone()[0]

#Получить всех пользователей из таблицы employee по id компании
def test_get_employee():
    select_all_query = sqlalchemy.select(employee).where(company_table.columns.id == company_id)
    select_all_result = connection.execute(select_all_query)
    assert(select_all_result.fetchall())

# Добавить пользователя
def test_create_employee():
    insertion_post = sqlalchemy.insert(employee).values([
        {"first_name":"Valentina", "last_name":"Balashova", "middle_name":"Alexsandrovna", "phone":"+79193369589", \
        "email":"lentina86@mail.ru", "birthdate":"2024-01-11T07:45:04.659Z", "avatar_url":"www", "company_id":company_id}
    ])
    result = connection.execute(insertion_post)
    select_query = sqlalchemy.select(employee).where(employee.columns.email == 'lentina86@mail.ru')
    result = connection.execute(select_query)
    employee_id = result.fetchone()[0]
    assert employee_id 

# Вывести пользователя по id
def test_get_employee_by_id():
    employee_id = employee.columns.id
    select_all_query = sqlalchemy.select(employee).where(employee.columns.id == employee_id)
    select_all_result = connection.execute(select_all_query)
    assert(select_all_result.fetchall())


# UPDATE пользователя по id
def test_update_employee():
    employee_id = employee.columns.id
    update_employee = sqlalchemy.update(employee).where(employee.columns.last_name == "Balashova").values({"last_name":"Dolgopolova"})
    connection.execute(update_employee)

#DELETE пользователя по id
def test_delete_employee():
    employee_id = employee.columns.id
    delete_employee = sqlalchemy.delete(employee).where(employee.columns.id == employee_id)
    connection.execute(delete_employee)

# Вывести всех пользователей после удаления
def test_employee_all():
    select_all_query = sqlalchemy.select(employee).where(company_table.columns.id == company_id)
    select_all_result = connection.execute(select_all_query)
    assert[select_all_result.fetchall()]