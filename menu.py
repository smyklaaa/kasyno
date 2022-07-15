from Black_Jack import BlackJack
from sign_in import SignIn
from log_in import LogIn

class Menu:
    """Klasa wyswietlajaca i pozwalajaca zarzadzac menu aplikacji"""

    def __init__(self):
        self.main_menu()


    def main_menu(self):
        """wyswietlanie menu """

        next = input("Logowanie\nRejstracja\nNajwieksze wygrane\n")
        while True:
            if next == "Logowanie":
                access_granted = self.access_granted()

                if access_granted:
                    next_log = input("Doładuj konto\nGraj\n")

                    if next_log == "Doładuj konto":
                        print("doladuj")

                    elif next_log == "Graj":
                        next_gry = input("Black Jack\nRuletka\nBaccarat\n")

                        if next_gry == "Black Jack":
                            game = BlackJack()
                            game.main()

                        elif next_gry == "Ruletka":
                            print("ru.etka")

                        elif next_gry == "Baccarat":
                            print("Baccarat")

            elif next == "Rejstracja":
                sign = SignIn()
                username = input("Podaj nazwe uzytkownika: ")
                password = self.check_password()
                account_value = self.check_account_values()
                sign.sign_in(username, password, account_value)


            elif next == "Najwieksze wygrane":
                print("20 najlepszych wynikow")

    def check_password(self):
        password = input("Podaj haslo: ")
        check_password = input("Powtorz haslo: ")
        while password != check_password:
            print("Hasla nie sa takie same\n")
            password = input("Podaj haslo: ")
            check_password = input("Powtorz haslo: ")
        return password

    def check_account_values(self):
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
        username = input("Podaj nazwe uzytkownika: ")
        password = input("Podaj haslo: ")
        for i in list_current_users:
            if i[0] == username and i[1] == password:
                return True
        return False

    def access_granted(self):
        log_in = LogIn()
        list_current_users = log_in.list_of_current_users()
        access_granted = self.check_login(list_current_users)
        while not access_granted:
            print("Niepoprawna proba zalogowania sprobuj jeszcze raz")
            access_granted = self.check_login(list_current_users)
        return access_granted



gra = Menu()