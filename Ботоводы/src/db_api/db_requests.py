import sqlite3


class Database:
    def __init__(self, db_path='shop_database.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users(
        id int NOT NULL,
        phone text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, phone: str = None):
        sql = 'INSERT INTO Users(id, phone) VALUES(?, ?)'
        parameters = (id, phone)
        self.execute(sql, parameters, commit=True)

    def select_user_info(self, **kwargs) -> list:
        sql = 'SELECT * FROM Users WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def select_all_users(self) -> list:
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    def update_user_phone(self, id: int, phone: str):
        sql = "UPDATE Users SET phone=? WHERE id=?"
        return self.execute(sql, parameters=(phone, id), commit=True)

    def delete_user(self, **kwargs):
        sql = "DELETE FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def delete_all(self):
        self.execute("DELETE FROM Users WHERE True", commit=True)

    def drop_all(self):
        self.execute("DROP TABLE Users", commit=True)

    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def __init__(self, db_path='food_database.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_foods(self):
        sql = """
        CREATE TABLE Foods(
        id int NOT NULL,
        name_food text,
        count_food int,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_food(self, id: int, name_food: str = None, count_food: int = None):
        sql = 'INSERT INTO Foods(id, name_food, count_food) VALUES(?, ?, ?)'
        parameters = (id, name_food, count_food)
        self.execute(sql, parameters, commit=True)

    def select_food_info(self, **kwargs) -> list:
        sql = 'SELECT * FROM Foods WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def select_all_foods(self) -> list:
        sql = "SELECT * FROM Foods"
        return self.execute(sql, fetchall=True)

    def update_food_name(self, id: int, name_food: str):
        sql = "UPDATE Foods SET name_food=? WHERE id=?"
        return self.execute(sql, parameters=(name_food, id), commit=True)

    def delete_food(self, **kwargs):
        sql = "DELETE FROM Foods WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def delete_all(self):
        self.execute("DELETE FROM Foods WHERE True", commit=True)

    def drop_all(self):
        self.execute("DROP TABLE Foods", commit=True)

    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
