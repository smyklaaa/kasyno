import sqlite3
from connection_data_base import DataBase
from os import getenv


class LogIn:
    """klasa obslugujaca logowanie urzytkownika"""

    def __init__(self):
        self.db = DataBase(getenv('DB_NAME'))

    def list_of_current_users(self):
        list_users = self.db.check_users()
        return list_users
