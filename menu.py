from Black_Jack import BlackJack

class Menu():
    """Klasa wyswietlajaca i pozwalajaca zarzadzac menu aplikacji"""

    def __init__(self):
        self.main_menu()


    def main_menu(self):
        """wyswietlanie menu """

        next = input("Logowanie\nRejstracja\nNajwieksze wygrane\n")
        while True:
            if next == "Logowanie":
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
                print("rejstracja")

            elif next == "Najwieksze wygrane":
                print("20 najlepszych wynikow")


gra = Menu()