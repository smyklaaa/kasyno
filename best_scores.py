from connection_data_base import DataBase
from os import getenv


class BestScores:
    """klasa odpowiedzialna za obsluge najlepszych wynikow """

    def __init__(self):
        self.db = DataBase(getenv('DB_NAME'))

    def show_the_results(self):
        """pokazuje liste 20 najlepszych wynikow"""

        list_of_best_scores = self.db.list_of_best_scores()
        i = 0
        for user in list_of_best_scores:
            i += 1
            print(f"{i}. Uzytkownik: {user[1]} - wynik: {user[0]}")

    def add_score(self, username, result):
        """metoda dodajaca wynik do tabeli najlepszych wynikow"""

        self.db.create_table('''CREATE TABLE IF NOT EXISTS best_scores 
        (username TEXT,
        result INT
        )
        ''')

        result_data = [username, result]

        self.db.add_score_to_best(result_data)

        if len(self.db.list_of_best_scores()) > 20:
            self.db.remove_score_from_best()
