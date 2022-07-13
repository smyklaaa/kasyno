import random
"""Klasa umożliwiająca rogrywke pokerowej gry Black Jack """

class BlackJack:

    def __init__(self):
        self.cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", ]
        self.croupier_cards = self.first_hand()
        self.player_cards = self.first_hand()
        self.croupier_symbol_cards = self.croupier_cards
        self.player_symbol_cards = self.player_cards
        self.bet_multiplier = 2

    def draw_card(self):
        # funkcja dobierajaca karte

        return random.choice(self.cards)

    def first_hand(self):
        # funkcja wybierajava pierwsze katyt gracza i krupiera

        # return map(self.draw_card, range(2))   #funkcje anonimowe poczytaj

        cards = []
        for i in range(2):
            cards.append(self.draw_card())
        return cards

    def check_figure(self, cards, ran):
        # funkcja sprawdzajaca czy wysosowano karte j q k lub a oraz zamienai je na liczby

        for i in range(ran):
            if cards[i] in ["J", "Q", "K"]:
                cards[i] = 10
            elif cards[i] == "A":
                cards[i] = 11
        return cards

    def check_as(self, amount, cards):
        #funkcja ktora po przekroczeniu 21 sprawdza czy w rece gracza jest as, jezeli tak zamienia jego wartosc na 1
        if amount > 21 and 11 in cards:
            amount -= 10
        return amount

    def show_hand(self, ):
        # funkcja wybierajaca pokazujaca karty
        sum_cards_player = self.sum_cards(self.player_cards)

        print(f"Twoje karty to {self.player_symbol_cards} ich suma wynosi: {sum_cards_player}")
        print(f"Karta krupiera  to {self.croupier_symbol_cards[0]}  ")

    def sum_cards(self, cards):
        # funkcja zwracajaca sume reki gracza/ komputera
        num_cards = self.check_figure(cards, len(cards))
        sum_cards = self.check_as(sum(num_cards), num_cards)
        return sum_cards

    def compare(self):
        # porownanie wynikow
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

    def result(self, result):
        # sprawdz switch/match
        if result == 0:
            print("Remis!")
        elif result == 2:
            print("Black Jack! Wygrałeś!")
        elif result == -1:
            print("Przegrales!")
        elif result == 1:
            print("Wygrales!")

    def croupier_hit(self, cards):
        #dobranie karty przez kuriera

        self.print_croupier()
        while self.sum_cards(cards) < 17:
            self.croupier_cards.append(self.draw_card())
            self.print_croupier()

    def print_croupier(self):
        #wyswietlanie kart krupiera
        print(f"Karty krupiera : {self.croupier_cards} ich suma: {self.sum_cards(self.croupier_cards)}")

    def hit(self, ):
        #dobranie kart przez gracza
        self.player_cards.append(self.draw_card())
        print(f"Twoje karty po dobraniu: {self.player_cards} ich suma: {self.sum_cards(self.player_cards)} ")

    def choose_action(self, ):
        # wybieramy nasz dalszy ruch dobrac karte , brak ruchu, podwojenie lub rozdwojenie
        if self.croupier_cards[0] == "A":
            print("Czy chcesz ubezpieczyc? ")
        else:
            while True:
                response = input("Wybierz dalszy ruch: \nH -Hit\nS - Stand\nD - Double\nSp - Split\n")
                if response == "H":
                    self.hit()

                    if self.sum_cards(self.player_cards) > 21:
                        self.croupier_hit(self.croupier_cards)
                        result_of_compere = self.compare()
                        self.result(result_of_compere)
                        break

                    if self.sum_cards(self.player_cards) == 21:
                        result_of_compere = self.compare()
                        if result_of_compere == 0:
                            self.print_croupier()
                        self.result(result_of_compere)
                        break

                elif response == "S":
                    self.croupier_hit(self.croupier_cards)
                    result_of_compere = self.compare()
                    self.result(result_of_compere)
                    break

                elif response == "D":
                    self.bet_multiplier *= 2

    def main(self):
        # funkcja głowna zarzadzajaca gra

        self.show_hand()
        self.choose_action()


gra = BlackJack()
gra.main()
