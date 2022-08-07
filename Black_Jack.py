from wallet import Wallet
from connection_data_base import DataBase
from os import getenv
from best_scores import BestScores
import random


class BlackJack:
    """Klasa umożliwiająca rogrywke pokerowej gry Black Jack """

    def __init__(self, username):
        self.cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", ]
        self.croupier_cards = self.first_hand()
        self.player_cards = self.first_hand()
        self.croupier_symbol_cards = self.croupier_cards
        self.player_symbol_cards = self.player_cards
        self.bet_multiplier = 1
        self.current_username = username
        self.account_balance = Wallet().return_account_balance(self.current_username)


    def draw_card(self):
        """metoda dobierajaca karte"""

        return random.choice(self.cards)

    def first_hand(self):
        """metoda wybierajava pierwsze katyt gracza i krupiera"""

        # return map(self.draw_card, range(2))   #funkcje anonimowe poczytaj

        cards = []
        for i in range(2):
            cards.append(self.draw_card())
        return cards

    def create_new_first_hand(self):
        self.croupier_cards = self.first_hand()
        self.player_cards = self.first_hand()
        self.croupier_symbol_cards = self.croupier_cards
        self.player_symbol_cards = self.player_cards

    def check_figure(self, cards, ran):
        """metoda sprawdzajaca czy wysosowano karte j q k lub a oraz zamienai je na liczby"""

        for i in range(ran):
            if cards[i] in ["J", "Q", "K"]:
                cards[i] = 10
            elif cards[i] == "A":
                cards[i] = 11
        return cards

    def check_as(self, amount, cards):
        """ metoda ktora po przekroczeniu 21 sprawdza czy w rece gracza jest as,
            jezeli tak zamienia jego wartosc na 1"""

        if amount > 21 and 11 in cards:
            amount -= 10
        return amount

    def show_hand(self, ):
        """metoda wybierajaca pokazujaca karty"""

        sum_cards_player = self.sum_cards(self.player_cards)

        print(f"Twoje karty to {self.player_symbol_cards} ich suma wynosi: {sum_cards_player}")
        print(f"Karta krupiera  to {self.croupier_symbol_cards[0]}  ")

    def sum_cards(self, cards):
        """metoda zwracajaca sume reki gracza/ komputera"""

        num_cards = self.check_figure(cards, len(cards))
        sum_cards = self.check_as(sum(num_cards), num_cards)
        return sum_cards

    def compare(self):
        """porownanie wynikow"""

        player_score = self.sum_cards(self.player_cards)
        croupier_score = self.sum_cards(self.croupier_cards)

        if player_score > 21 and croupier_score > 21:
            return -1

        if player_score == croupier_score:
            return 0
        elif croupier_score == 21:
            return -1
        elif player_score == 21:
            return 2
        elif player_score > 21:
            return -1
        elif croupier_score > 21:
            return 1
        elif player_score > croupier_score:
            return 1
        else:
            return -1

    def result(self, result, bet):
        """sprawdz switch/match"""

        if result == 0:
            print(f"Remis!\nTwój stan konta wynosi: {self.account_balance}")

        elif result == 2:
            bet *= self.bet_multiplier
            self.account_balance += bet
            best_score = BestScores()
            best_score.add_score(self.current_username, bet)
            print(f"Black Jack! Wygrałeś!\nTwój stan konta wynosi: {self.account_balance}")

        elif result == -1:
            self.account_balance -= bet
            print(f"Przegrales!\nTwój stan konta wynosi: {self.account_balance}")

        elif result == 1:
            bet *= self.bet_multiplier
            self.account_balance += bet
            best_score = BestScores()
            best_score.add_score(self.current_username, bet)
            print(f"Wygrałeś!\nTwój stan konta wynosi: {self.account_balance}")

    def croupier_hit(self, cards):
        """dobranie karty przez kuriera"""

        self.print_croupier()
        while self.sum_cards(cards) < 17:
            self.croupier_cards.append(self.draw_card())
            self.print_croupier()

    def print_croupier(self):
        """wyswietlanie kart krupiera"""

        print(f"Karty krupiera : {self.croupier_cards} ich suma: {self.sum_cards(self.croupier_cards)}")

    def hit(self, ):
        """dobranie kart przez gracza"""
        self.player_cards.append(self.draw_card())
        print(f"Twoje karty po dobraniu: {self.player_cards} ich suma: {self.sum_cards(self.player_cards)} ")

    def choose_action(self, bet):
        """wybieramy nasz dalszy ruch dobrac karte , brak ruchu, podwojenie lub rozdwojenie"""

        while True:
            response = input("Wybierz dalszy ruch: \nH -Hit\nS - Stand\nD - Double\n")
            if response == "D":
                self.bet_multiplier = 2

            if response == "H":
                self.hit()

                if self.sum_cards(self.player_cards) > 21:
                    self.croupier_hit(self.croupier_cards)
                    result_of_compere = self.compare()
                    self.result(result_of_compere, bet)
                    break

                if self.sum_cards(self.player_cards) == 21:
                    result_of_compere = self.compare()
                    if result_of_compere == 0:
                        self.print_croupier()
                    self.result(result_of_compere, bet)
                    break

            elif response == "S":
                self.croupier_hit(self.croupier_cards)
                result_of_compere = self.compare()
                self.result(result_of_compere, bet)
                break


    def new_game(self):
        """metoda zerujaca karty krupiera i gracza"""

        self.croupier_cards = []
        self.player_cards = []

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


    def main(self):
        """metoda głowna zarzadzajaca gra"""

        new_game = "t"
        i = 1
        while new_game == "t":
            bet = self.make_bet()
            if i > 1:
                self.new_game()
                self.create_new_first_hand()
            self.show_hand()
            self.choose_action(bet)
            i = i+1
            new_game = input("Czy chcesz zagrac jeszcze raz? t/n\n")
            while new_game not in ["t","n"]:
                new_game = input("nie rozumiem, czy chcesz zagrac jeszcze raz? t/n\n")
            if new_game == "n":
                i = 1
                db = DataBase(getenv('DB_NAME'))
                db.update_account_balance(self.account_balance,self.current_username)


