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
        """metoda tworzaca tabele """

        self.cursor.execute(table)
        self.connection.commit()

    def insert_data(self, sign_data):
        """metoda dodajaca dane do tabeli """

        self.cursor.execute(''' INSERT INTO log_data 
                                VALUES(?,?,?)''', sign_data)
        self.connection.commit()

    def check_users(self):
        """metoda zwracajaca liste nazw i hasel urzytkownikow """

        self.cursor.execute(''' SELECT username,password 
                                FROM log_data''')
        users_data = self.cursor.fetchall()
        return users_data

    def check_account(self):
        """metoda zwracajaca nazwe uzytkownika i wraz ze stanem konta """

        self.cursor.execute(''' SELECT username,account 
                                FROM log_data''')
        users_data = self.cursor.fetchall()
        return users_data

    def update_account_balance(self, amount, username):
        """metoda aktualizujaca stan konta uzytkownika po doladowaniu konta"""

        updated_data = [amount, username]

        self.cursor.execute(''' UPDATE log_data
                                SET account = ?
                                WHERE username = ? 
                            ''', updated_data)
        self.connection.commit()

    def list_of_best_scores(self):
        """metoda zwracajaca liste najlepszych wynikow """

        self.cursor.execute(''' SELECT result,username
                                FROM best_scores
                                ORDER BY result DESC''')
        users_data = self.cursor.fetchall()
        return users_data

    def add_score_to_best(self, sign_data):
        """metoda dodajaca wynik do tabeli najlepszych wynikow """

        self.cursor.execute(''' INSERT INTO best_scores
                                VALUES(?,?)''', sign_data)
        self.connection.commit()

    def remove_score_from_best(self):
        """metoda usuwajaca najgorszy wynik z tabeli najlepszych wynikow """

        self.cursor.execute(f''' DELETE FROM best_scores
                                WHERE result NOT IN
                                (
                                SELECT result FROM best_scores
                                ORDER BY result DESC LIMIT 20
                                )
                                ''')
        self.connection.commit()
