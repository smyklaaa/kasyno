import sqlite3
from connection_data_base import DataBase
from os import getenv


class SignIn:
    """Klasa pozwalajaca na zarejstrowanie użytkownika"""

    def __init__(self):
        self.users = open("user_list","a+")

    def sign_in(self, username, password, account_value):
        """metoda zapisujaca uzytkownika w bazie danych sprawdzajac czy nazwa jest unikatowa"""

        db = DataBase(getenv('DB_NAME'))
        db.create_table('''CREATE TABLE IF NOT EXISTS log_data 
        (username TEXT PRIMARY KEY, 
        password TEXT, 
        account INT)
        ''')
        log_data = [username, password, account_value]
        name = True
        while name:
            try:
                db.insert_data(log_data)
                name = False
            except sqlite3.IntegrityError:
                new_username = input("Nazwa uzytkownika jest zajeta, podaj inna nazwe:")
                log_data = [new_username, password, account_value]

