from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import text

class BD:
    __scripts = {
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
        self.db = create_engine(connection_string)
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.db)
        self.table = Table('employee', self.metadata, autoload=True)

    def create_table(self):
        with self.db.connect() as connection:
            connection.execute(self.__scripts["create"])

    def get_employees(self):
        with self.db.connect() as connection:
            return connection.execute(self.__scripts["select"]).fetchall()

    def insert_employee(self, first_name, last_name, phone, company_id):
        with self.db.connect() as connection:
            return connection.execute(self.__scripts["insert"],
                                 first_name,
                                 last_name,
                                 phone,
                                 company_id)

    def update_employee(self, employee_id, first_name, last_name, middle_name, phone, email, avatar_url):
        with self.db.connect() as connection:
            return connection.execute(self.__scripts["update"],
                                    employee_id = employee_id,
                                    first_name = first_name,
                                    last_name = last_name,
                                    middle_name = middle_name,
                                    phone = phone,
                                    email = email,
                                    avatar_url = avatar_url)

    def delete_employee(self, employee_id):
        with self.db.connect() as connection:
            return connection.execute(self.__scripts["delete"], employee_id=employee_id)
        