import sqlite3
from logger import get_logger

logger = get_logger()

CREATE_BRAND_TABLE = """CREATE TABLE IF NOT EXISTS brand (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    name varchar
                    ); """

CREATE_MODEL_TABLE = """CREATE TABLE IF NOT EXISTS car (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    model varchar,
                    release_year integer,
                    brand_id integer,
                    FOREIGN KEY(brand_id) REFERENCES brand(id)
                    ); """


def create_tables():
    db_connection = sqlite3.connect('hw_16.db')
    cursor = db_connection.cursor()

    cursor.execute(CREATE_BRAND_TABLE)
    cursor.execute(CREATE_MODEL_TABLE)
    cursor.close()

    db_connection.commit()
    db_connection.close()


create_tables()


# CRUD realisation
class ParentCRUD:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = self.__get_connection()
        self.cursor = self.__get_cursor()

    def __get_connection(self):
        try:
            connection = sqlite3.connect(self.db_name)
            logger.error(f'Connection to db {self.db_name} successfully created!')
            return connection
        except sqlite3.Error as e:
            logger.warning(str(e))
            raise e

    def __get_cursor(self):
        return self.connection.cursor()


class BrandCRUD(ParentCRUD):

    def create(self, name: str):
        insert_query = "INSERT INTO brand(name) VALUES (?)"
        self.connection.execute(insert_query, (name,))
        self.connection.commit()
        logger.info(f'Brand {name} successfully created!')
        return self.cursor.lastrowid

    def read(self, id_: int):
        try:
            select_query = "SELECT * FROM brand WHERE id = ?"
            execute = self.connection.execute(select_query, (id_,))
            result = execute.fetchall()
            self.connection.commit()
            return result
        except sqlite3.Error as id_read_error:
            logger.warning(str(id_read_error))
            raise id_read_error

    def update(self, id_: int, name: str):
        update_query = "UPDATE brand SET name = ? WHERE id = ?"
        self.connection.execute(update_query, (name, id_))
        self.connection.commit()
        logger.info(f'Brand {name} successfully update!')

    def delete(self, id_: int, name: str):
        delete_query = "DELETE FROM brand WHERE id = ?"
        self.connection.execute(delete_query, (id_,))
        self.connection.commit()
        logger.info(f'Brand {name} successfully deleted')


class CarCRUD(ParentCRUD):

    def create(self, model: str, release_year: int, brand_id: int):
        insert_query = "INSERT INTO car (model, release_year, brand_id) VALUES (?, ?, ?)"
        self.connection.execute(insert_query, (model, release_year, brand_id))
        self.connection.commit()
        logger.info(f'Model {model} successfully created!')
        return self.cursor.lastrowid

    def read(self, id_: int):
        try:
            select_query = "SELECT * FROM car WHERE id = ?"
            execute = self.connection.execute(select_query, (id_,))
            result = execute.fetchall()
            self.connection.commit()
            return result
        except sqlite3.Error as id_read_error:
            logger.warning(str(id_read_error))
            raise id_read_error

    def update(self, id_: int, model: str, release_year: int, brand_id: int):
        update_query = "UPDATE car SET model = ?, release_year = ?, brand_id = ? WHERE id = ?"
        self.connection.execute(update_query, (model, release_year, brand_id, id_))
        self.connection.commit()
        logger.info(f'Brand {model} successfully update!')

    def delete(self, id_: int, model: str):
        delete_query = "DELETE FROM car WHERE id = ?"
        self.connection.execute(delete_query, (id_,))
        self.connection.commit()
        logger.info(f'Brand {model} successfully deleted')


if __name__ == '__main__':
    brand_db = BrandCRUD(db_name='hw_16.db')
    car_db = CarCRUD(db_name='hw_16.db')

    brand_id_ = brand_db.create(name='Tesla')
    brand_id_2 = brand_db.create(name='Mazda')
    car_id = car_db.create(model='three', release_year=2019, brand_id=1)
    car_id_2 = car_db.create(model='s60', release_year=2013, brand_id=2)

    brand_read = brand_db.read(1)
    car_read = car_db.read(1)

    brand_db.update(id_=2, name='Volvo')
    car_db.update(id_=2, model='s40', release_year=2017, brand_id=2)

    brand_db.delete(id_=1, name='Tesla')

