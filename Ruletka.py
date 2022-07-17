import random
from wallet import Wallet
from os import getenv
from connection_data_base import DataBase


class Ruletka:
    """Klasa umozliwiajaca gre w ruletke"""

    def __init__(self, username):
        self.current_username = username
        self.account_balance = Wallet().return_account_balance(self.current_username)
        self.one_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                           22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        self.even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        self.first_dozen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.second_dozen = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        self.third_dozen = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.first_half = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.second_half = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.first_column = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        self.second_column = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        self.third_column = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        self.board = "3 6 9 12   15 18 21 24   27 30 33 36\n2 5 8 11   14 17 20 23   26 29 32 35 \n" \
                     "1 4 7 10   13 16 19 22   25 28 31 34"

    def main(self):
        """metoda głowna zarzadzajaca gra"""

        new_game = "t"
        while new_game == "t":
            bet = self.make_bet()
            print(self.board)

            self.check_result(self.select_bet(),self.draw_number(), bet)

            new_game = input("Czy chcesz zagrac jeszcze raz? t/n\n")
            while new_game not in ["t", "n"]:
                new_game = input("nie rozumiem, czy chcesz zagrac jeszcze raz? t/n\n")
            if new_game == "n":
                db = DataBase(getenv('DB_NAME'))
                db.update_account_balance(self.account_balance, self.current_username)

    def check_bet_value(self):
        """metoda sprawdza czy wartosc zakładu ktorą podaje uzytkownik jest nieujemna liczbą"""

        while True:
            try:
                account_value = input("Za jaką kwotę chcesz obstawic zakład? : ")
                account_value = int(account_value)
                break

            except ValueError:
                print("Podales wartosc tekstowa zamiast liczby")

        while int(account_value) < 0:
            account_value = input("Wartosc zakładu nie moze byc ujemna, podaj prawidlowa wartosc: ")
        return int(account_value)

    def make_bet(self):
        """funkcja tworzaca zakład """

        bet = self.check_bet_value()
        while bet > self.account_balance:
            print("Nie masz wystarczajaca środków na koncie")
            bet = self.check_bet_value()

        return bet

    def draw_number(self):
        """metoda symulujaca zachowanie kulki ruletki """

        number = random.choice(self.one_number)
        return number

    def select_bet(self):
        """metoda przyjmujaca zaklad i sprawdzajaca jego wynik"""

        user_numbers = input("Wybierz numer przy obcji na ktora obstawiasz:\n(1)Czerwone, (2)Czarne , "
                        "(3)Parzyste, (4)Nieparzyste, "
                        "(5)Kolumna1, (6)Kolumna2, (7)Kolumna3, \n(8)Tuzin1, (9)Tuzin2, (10)Tuzin3, "
                        "(11)Pierwsza polowa<1-18>, (12)Druga polowa<19-36>, (13)Pojedynczy numer\n")

        while user_numbers not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]:
            print("Nie zrozumiałem")
            user_numbers = input("Wybierz numer przy obcji na ktora obstawiasz:\n(1)Czerwone, (2)Czarne , "
                                 "(3)Parzyste, (4)Nieparzyste, "
                                 "(5)Kolumna1, (6)Kolumna2, (7)Kolumna3, \n(8)Tuzin1, (9)Tuzin2, (10)Tuzin3, "
                                 "(11)Pierwsza polowa<1-18>, (12)Druga polowa<19-36>, (13)Pojedynczy numer\n")
        user_numbers = int(user_numbers)
        return user_numbers

    def check_result(self, user_numbers, number, bet):
        """metoda sprawdzajaca wygrana """

        if user_numbers == 1:
            print(f"Wylosowana liczaba: {number}")
            if number in self.red:
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 2:
            print(f"Wylosowana liczaba: {number}")
            if number in self.black:
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 3:
            print(f"Wylosowana liczaba: {number}")
            if number in self.even_numbers:
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 4:
            print(f"Wylosowana liczaba: {number}")
            if number in self.odd_numbers:
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 5:
            print(f"Wylosowana liczaba: {number}")
            if number in self.first_column:
                bet *= 2
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 6:
            print(f"Wylosowana liczaba: {number}")
            if number in self.second_column:
                bet *= 2
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 7:
            print(f"Wylosowana liczaba: {number}")
            if number in self.third_column:
                bet *= 2
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 8:
            print(f"Wylosowana liczaba: {number}")
            if number in self.first_dozen:
                bet *= 2
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 9:
            print(f"Wylosowana liczaba: {number}")
            if number in self.second_dozen:
                bet *= 2
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 10:
            print(f"Wylosowana liczaba: {number}")
            if number in self.third_dozen:
                bet *= 2
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 11:
            print(f"Wylosowana liczaba: {number}")
            if number in self.first_half:
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 12:
            print(f"Wylosowana liczaba: {number}")
            if number in self.second_half:
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")

        elif user_numbers == 13:
            user_number = input("Podaj jaki numer obstawiasz: ")
            print(f"Wylosowana liczaba: {number}")

            if int(user_number) == number:
                bet *= 35
                self.account_balance += bet
                print(f"Wygrałes! Twoj stan konta wynosi {self.account_balance}")
            else:
                self.account_balance -= bet
                print(f"Przegrales! Twoj stan konta wynosi {self.account_balance}")


