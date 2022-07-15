import sqlite3
from connection_data_base import DataBase
from os import getenv


class Wallet:
    """Klasa obsługujaca portfel gracza"""

    def __init__(self):
        self.db = DataBase(getenv('DB_NAME'))

    def check_account(self, username):
        users_data = self.db.check_account()
        for i in users_data:
            if username == i[0]:
                print(f"Twoj stan konta wynosi: {i[1]} ")

    def increase_account(self):
        pass

