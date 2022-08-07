from Black_Jack import BlackJack
from sign_in import SignIn
from log_in import LogIn
from wallet import Wallet
from Baccarat import Baccarat
from Ruletka import Ruletka
from best_scores import BestScores
import os

class Menu:
    """Klasa wyswietlajaca i pozwalajaca zarzadzac menu aplikacji"""

    def __init__(self):
        self.main_menu()
        self.current_login_username = ""


    def main_menu(self):
        """wyswietlanie menu """

        while True:
            what_next = input("Logowanie\nRejstracja\nNajwieksze wygrane\nWylacz\n")

            while what_next not in ["Logowanie", "logowanie","rejstracja","Rejstracja", "najwieksze wygrane",
                                    "Najwieksze wygrane","najwieksze wygrane","wylacz","Wylacz","wyłącz","Wyłącz"]:
                what_next = input("Logowanie\nRejstracja\nNajwieksze wygrane\nWylacz\n")
            log_out = False

            os.system("cls")
            while True:
                if what_next in ["Logowanie", "logowanie"]:
                    if log_out:
                        break
                    access_granted = self.access_granted()
                    os.system("cls")

                    while True:
                        if access_granted:
                            next_log = input("Stan konta\nDoładuj konto\nGraj\nWyloguj sie\n")

                            if next_log in ["Doładuj konto", "doładuj konto", "Doladuj konto"]:
                                os.system("cls")
                                new_account_balance = Wallet()
                                new_account_balance.increase_account(self.current_login_username)

                            elif next_log in ["Wyloguj sie", "wyloguj sie"]:
                                log_out = True
                                os.system("cls")
                                break

                            elif next_log in ["Stan konta", "stan konta"]:
                                os.system("cls")
                                account_balance = Wallet()
                                account_balance.check_account(self.current_login_username)

                            elif next_log in ["Graj", "graj"]:
                                os.system("cls")
                                while True:
                                    next_gry = input("Black Jack\nRuletka\nBaccarat\nCofnij\n")
                                    os.system("cls")

                                    if next_gry in ["Black Jack","black jack"]:
                                        game = BlackJack(self.current_login_username)
                                        game.main()
                                        os.system("cls")

                                    elif next_gry in ["Ruletka", "ruletka"]:
                                        game = Ruletka(self.current_login_username)
                                        game.main()
                                        os.system("cls")

                                    elif next_gry in ["Baccarat", "baccarat"]:
                                        game = Baccarat(self.current_login_username)
                                        game.baccarat_main()
                                        os.system("cls")

                                    elif next_gry in ["Cofnij", "cofnij"]:
                                        os.system("cls")
                                        break

                elif what_next in ["Rejstracja", "rejstracja"]:
                    sign = SignIn()
                    username = input("Podaj nazwe uzytkownika: ")
                    password = self.check_password()
                    account_value = self.check_account_values()
                    sign.sign_in(username, password, account_value)
                    os.system("cls")
                    break

                elif what_next in ["Najwieksze wygrane", "najwieksze wygrane"]:
                    best = BestScores()
                    best.show_the_results()
                    break

    def check_password(self):
        """ metoda pobiera haslo od uzytkownika i sprawdza czy nie wystopil blad przy wpisywaniu,po czym je zwraca"""

        password = input("Podaj haslo: ")
        check_password = input("Powtorz haslo: ")
        while password != check_password:
            print("Hasla nie sa takie same\n")
            password = input("Podaj haslo: ")
            check_password = input("Powtorz haslo: ")
        return password

    def check_account_values(self):
        """metoda sprawdza czy wartosc konta ktora podaje uzytkownik jest nieujemna liczba"""

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


    def check_login(self, list_current_users):
        """ metoda pobierajaca nazwe uzytkownika i haslo i sprawdzajaca czy intnieje w bazie danych """

        username = input("Podaj nazwe uzytkownika: ")
        password = input("Podaj haslo: ")
        for i in list_current_users:
            if i[0] == username and i[1] == password:
                self.current_login_username = username
                return True
        return False

    def access_granted(self):
        """ metoda obslugujaca proces logowania sie , przyznaje dostep do konta po poprawnym zalogowaniu """

        log_in = LogIn()
        list_current_users = log_in.list_of_current_users()
        access_granted = self.check_login(list_current_users)
        while not access_granted:
            print("Niepoprawna proba zalogowania sprobuj jeszcze raz")
            access_granted = self.check_login(list_current_users)
        return access_granted
