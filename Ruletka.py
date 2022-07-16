import random
from wallet import Wallet
from os import getenv
from connection_data_base import DataBase


class Ruletka:
    """Klasa umozliwiajaca gre w ruletke"""

    def __init__(self, username):
        self.bet_multiplier = 2
        self.current_username = username
        self.account_balance = Wallet().return_account_balance(self.current_username)
        self.one_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                               22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        self.even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        self.first_dozen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.second_dozen = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        self.third_dozen = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19,  21, 23, 25, 27, 30, 32, 34, 36]
        self.black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.first_half = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.second_half = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.first_column = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        self.second_column = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        self.third_column = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        self.board = "3 6 9 12 15 18 21 24 27 30 33 36\n2 5 8 11 14 17 20 23 26 29 32 35 \n" \
                     "1 4 7 10 13 16 19 22 25 28 31 34"


    def main(self):
        print(self.board)


gra = Ruletka("janek")
gra.main()