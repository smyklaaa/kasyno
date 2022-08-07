from Black_Jack import BlackJack
from os import getenv
from connection_data_base import DataBase
from best_scores import BestScores

class Baccarat(BlackJack):
    """klasa tworzaca rozgrywke w pokerowa gra baccarat"""

    def __init__(self, username):
        super().__init__(username)



    def baccarat_main(self):
        """metoda głowna zarzadzajaca gra"""

        new_game = "t"
        i = 1
        while new_game == "t":
            bet = self.make_bet()
            if i > 1:
                self.new_game()
                self.create_new_first_hand()
            if self.show_hand_baccarat(bet):
                self.choose_action_baccarat(bet)

            i = i+1
            new_game = input("Czy chcesz zagrac jeszcze raz? t/n\n")
            while new_game not in ["t", "n"]:
                new_game = input("nie rozumiem, czy chcesz zagrac jeszcze raz? t/n\n")
            if new_game == "n":
                i = 1
                db = DataBase(getenv('DB_NAME'))
                db.update_account_balance(self.account_balance, self.current_username)

    def sum_cards_baccarat(self, cards):
        """metoda zwracajaca sume reki gracza/ komputera"""

        num_cards = self.check_figure_baccarat(cards, len(cards))
        sum_cards = sum(num_cards) % 10
        return sum_cards

    def check_figure_baccarat(self, cards, ran):
        """metoda sprawdzajaca czy wysosowano karte j q k lub a oraz zamienai je na liczby"""

        for i in range(ran):
            if cards[i] in ["J", "Q", "K",  "10"]:
                cards[i] = 0
            elif cards[i] == "A":
                cards[i] = 1
        return cards

    def show_hand_baccarat(self,bet):
        """metoda wybierajaca pokazujaca karty"""

        check = True
        sum_cards_player = self.sum_cards_baccarat(self.player_cards)
        sum_cards_croupier = self.sum_cards_baccarat(self.croupier_cards)

        print(f"Twoje karty to {self.player_symbol_cards} ich wartos w grze wynosi: {sum_cards_player}")
        print(f"Karta krupiera  to {self.croupier_symbol_cards}  ich wartos w grze wynosi: {sum_cards_croupier} ")

        if sum_cards_croupier == 9 and sum_cards_player < sum_cards_croupier:
            self.account_balance -= bet
            print(f"Przegrales!\nTwój stan konta wynosi: {self.account_balance}")
            check = False

        elif sum_cards_player == 9 and sum_cards_player > sum_cards_croupier:
            self.account_balance += bet
            print(f"Wygrałeś!\nTwój stan konta wynosi: {self.account_balance}")
            check = False

        return check

    def compare_baccarat(self):
        """porownanie wynikow"""

        player_score = self.sum_cards_baccarat(self.player_cards)
        croupier_score = self.sum_cards_baccarat(self.croupier_cards)

        if player_score == 9 and croupier_score == 9:
            return 0
        elif player_score == 9:
            return 1
        elif croupier_score == 9:
            return -1
        elif croupier_score == player_score:
            return 0
        elif croupier_score > player_score:
            return -1
        elif croupier_score < player_score:
            return 1

    def choose_action_baccarat(self, bet):
        """wybieramy nasz dalszy ruch dobrac karte , brak ruchu, podwojenie lub rozdwojenie"""

        while True:
            response = input("Wybierz dalszy ruch: \nH -Hit\nS - Stand\n")

            if response == "H":
                self.hit_baccarat()
                self.croupier_hit_baccarat()
                result_of_compere = self.compare_baccarat()
                self.result_baccarat(result_of_compere, bet)
                break

            elif response == "S":
                result_of_compere = self.compare_baccarat()
                self.result_baccarat(result_of_compere, bet)
                break

    def hit_baccarat(self):
        """dobranie kart przez gracza"""

        self.player_cards.append(self.draw_card())
        print(f"Karty po dobraniu: {self.player_cards} ich suma: {self.sum_cards_baccarat(self.player_cards)} ")

    def croupier_hit_baccarat(self):
        """dobranie karty przez kuriera"""

        self.print_croupier_baccarat()
        if self.sum_cards_baccarat(self.croupier_cards) < 5 or \
                self.sum_cards_baccarat(self.croupier_cards) < self.sum_cards_baccarat(self.player_cards):

            self.croupier_cards.append(self.draw_card())
            self.print_croupier_baccarat()

    def print_croupier_baccarat(self):
        """wyswietlanie kart krupiera"""

        print(f"Karty krupiera : {self.croupier_cards} ich wartosc: {self.sum_cards_baccarat(self.croupier_cards)}")

    def result_baccarat(self, result, bet):
        """sprawdz switch/match"""

        if result == 0:
            print(f"Remis!\nTwój stan konta wynosi: {self.account_balance}")

        elif result == -1:
            self.account_balance -= bet
            print(f"Przegrales!\nTwój stan konta wynosi: {self.account_balance}")

        elif result == 1:
            self.account_balance += bet
            best_score = BestScores()
            best_score.add_score(self.current_username, bet)
            print(f"Wygrałeś!\nTwój stan konta wynosi: {self.account_balance}")


