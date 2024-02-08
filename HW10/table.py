from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import text

class Table:
    scripts = {
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
            RETURNING id
        """),
        "update": text("""
            UPDATE employee SET first_name = :first_name, last_name = :last_name,
            middle_name = :middle_name, phone = :phone, email = :email, avatar_url = :avatar_url
            WHERE id = :employee_id
        """),
        "get_employee_by_id": text("SELECT * FROM employee WHERE id = :employee_id"),
        "delete": text("DELETE FROM employee WHERE id = :employee_id")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.db)
        self.table = Table('employee', self.metadata, autoload=True)

    def create_table(self):
        with self.db.connect() as connection:
            connection.execute(self.scripts["create"])
    
    def get_employees(self):
        """
            Вывести список пользователей
        """
        with self.db.connect() as connection:
            return list(connection.execute(self.scripts["select"]).mappings())
    
    def insert_employee(self, first_name, last_name, phone, company_id):
        """
            Добавить нового пользователя
        """
        with self.db.connect() as connection:
            query = self.scripts["insert"]
            result = connection.execute(query, {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'company_id': company_id
            })
            connection.commit()
            return result.fetchone()[0]
    
    def update_employee(self, employee_id, first_name, last_name, middle_name, phone, email, avatar_url):
        """
            Отредактировать пользователя по id
        """
        with self.db.connect() as connection:
            connection.execute(self.scripts["update"], {
                'employee_id': employee_id,
                'first_name': first_name,
                'last_name': last_name,
                'middle_name': middle_name,
                'phone': phone,
                'email': email,
                'avatar_url': avatar_url})
            connection.commit()

    def get_employee_by_id(self, employee_id):
        """
            Вывести список пользователей
        """
        with self.db.connect() as connection:
            result = connection.execute(self.scripts["get_employee_by_id"], {'employee_id': employee_id})
        return result.fetchone()

    def delete_employee(self, employee_id):
        """
            Удалить пользователя по id
        """
        with self.db.connect() as connection:
            connection.execute(self.scripts["delete"], {'employee_id': employee_id})
            connection.commit()