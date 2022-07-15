import sqlite3
from dotenv import load_dotenv
load_dotenv()


class DataBase:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, table):
        self.cursor.execute(table)
        self.connection.commit()

    def insert_data(self, sign_data):
        self.cursor.execute('''INSERT INTO log_data VALUES(?,?,?)''', sign_data)
        self.connection.commit()

    def check_users(self):
        self.cursor.execute('''SELECT username,password FROM log_data''')
        users_data = self.cursor.fetchall()
        return users_data
