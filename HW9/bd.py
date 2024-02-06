from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import text


class BD:
    script = {
        "create": text("""
            CREATE TABLE IF NOT EXISTS employee (
                id SERIAL PRIMARY KEY,
                is_active BOOLEAN DEFAULT TRUE,
                create_timestamp TIMESTAMP DEFAULT now(),
                change_timestamp TIMESTAMP DEFAULT now(),
                first_name VARCHAR(20) NOT NULL,
                last_name VARCHAR(20) NOT NULL,
                middle_name VARCHAR(20),
                phone VARCHAR(15) NOT NULL,
                email VARCHAR(256),
                avatar_url VARCHAR(1024),
                company_id INTEGER NOT NULL
            )
        """),
        "select": text("SELECT * FROM employee"),
        "insert": text("""
            INSERT INTO employee (first_name, last_name, phone, company_id)
            VALUES (:first_name, :last_name, :phone, :company_id)
        """),
        "update": text("""
            UPDATE employee SET first_name = :first_name, last_name = :last_name,
            middle_name = :middle_name, phone = :phone, email = :email, avatar_url = :avatar_url
            WHERE id = :employee_id
        """),
        "delete": text("DELETE FROM employee WHERE id = :employee_id")
    }

    def __init__(self, connection_string):
        self.__db__ = create_engine(connection_string)
        self.metadata = MetaData()
        self.metadata.bind = self.__db__
        self.table = Table('employee', self.metadata, autoload_with=self.__db__)

    def create_table(self):
        self.__db__.execute(self.script["create"])

    def get_employees(self):
        return self.__db__.execute(self.script["select"]).fetchall()

    def insert_employee(self, first_name, last_name, phone, company_id):
        return self.__db__.execute(self.script["insert"], {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'company_id': company_id
        })

    def update_employee(self, employee_id, first_name, last_name, middle_name, phone, email, avatar_url):
        return self.__db__.execute(self.script["update"], {
            'employee_id': employee_id,
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'phone': phone,
            'email': email,
            'avatar_url': avatar_url
        })

    def delete_employee(self, employee_id):
        return self.__db__.execute(self.script["delete"], {'employee_id': employee_id})