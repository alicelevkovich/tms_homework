import sqlite3

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS user (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    firstname varchar(255),
                    lastname varchar(255), 
                    age integer 
                    ) """


def create_users_table():
    db_connection = sqlite3.connect('cw_15.db')
    cursor = db_connection.cursor()

    cursor.execute(CREATE_USERS_TABLE)
    cursor.close()

    db_connection.commit()
    db_connection.close()


create_users_table()


# CRUD realisation

class SQLiteCRUD:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = self.get_connection()

    def get_connection(self):
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            with open('log.txt', 'a+') as log_file:
                log_file.write(str(e))

    def create(self, first_name: str, last_name: str):
        insert_query = "INSERT INTO user(firstname, lastname) VALUES (?, ?)"
        self.connection.execute(insert_query, (first_name, last_name))
        self.connection.commit()

    def read(self, id: int):
        try:
            select_query = "SELECT * FROM user WHERE id = ?"
            execute = self.connection.execute(select_query, (id,))
            result = execute.fetchall()
            self.connection.commit()
            return result
        except sqlite3.Error as id_read_error:
            with open('log.txt', 'a+') as log_file:
                log_file.write(str(id_read_error))

    def update(self, id: int, first_name: str, last_name: str, age: int):
        update_query = "UPDATE user SET firstname = ?, lastname = ?, age = ? " \
                       "WHERE id = ?"
        self.connection.execute(update_query, (first_name, last_name, age, id))
        self.connection.commit()

    def delete(self, id: int):
        try:
            delete_query = "DELETE FROM user WHERE id = ?"
            self.connection.execute(delete_query, (id,))
            self.connection.commit()
        except sqlite3.Error as id_delete_error:
            with open('log.txt', 'a+') as log_file:
                log_file.write(str(id_delete_error))


if __name__ == '__main__':
    sqlitecrud = SQLiteCRUD('cw_15.db')
    sqlitecrud.create('Edwin', 'Harman')
    sqlitecrud.create('Alan', 'Cooper')
    sqlitecrud.read(2)
    sqlitecrud.update(2, 'Eric', 'Cooper', 23)
    sqlitecrud.delete(1)





