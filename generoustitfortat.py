from strategy import Strategy
import random


class GenerousTitForTat(Strategy):

    def __init__(self):
        self.player_number = None

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if not history:
            return 'c'

        opponent_last_move = history[-1][1] if self.player_number == 1 else history[-1][0]

        if opponent_last_move == 'd' and random.random() < 0.9:
            return 'd'

        return 'c'


    def get_name(self):
        return 'Generous Tit For Tat'