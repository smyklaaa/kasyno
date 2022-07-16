import sqlite3
from connection_data_base import DataBase
from os import getenv



class Wallet:
    """Klasa obsługujaca portfel gracza"""

    def __init__(self):
        self.db = DataBase(getenv('DB_NAME'))

    def check_account(self, username):
        """metoda zwracjajaca stan konta dla zalogowanego uzytkownika """

        users_data = self.db.check_account()
        for user in users_data:
            if username == user[0]:
                print(f"Twoj stan konta wynosi: {user[1]} ")
                break

    def increase_account(self, username):
        """metoda pozwalajaca doładować konto zalogowanemu użytkownikowi """

        users_data = self.db.check_account()
        for user in users_data:
            if username == user[0]:
                amount = self.check_account_values()
                amount += int(user[1])
                break
        self.db.update_account_balance(amount, username)
        print(f"Twoja wpłata została zaakceptowana, twój obecny balans wynosi: {amount}")


    def check_account_values(self):
        """metoda sprawdza czy wartosc konta ktorą podaje uzytkownik jest nieujemna liczbą"""

        while True:
            try:
                account_value = input("Podaj ile chcesz wplacic na swoje konto: ")
                account_value = int(account_value)
                break

            except ValueError:
                print("Podales wartosc tekstowa zamiast liczby")

        while int(account_value) < 0:
            account_value = input("Wartosc konta nie moze byc ujemna, podaj prawidlowa wartosc: ")
        return account_value

    def return_account_balance(self, username):
        """metoda zwracajaca wartosc konta zalogowanego uzytkownika jako intiger"""

        users_data = self.db.check_account()
        for user in users_data:
            if username == user[0]:
                return int(user[1])
