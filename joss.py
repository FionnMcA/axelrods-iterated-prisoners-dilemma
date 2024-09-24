from strategy import Strategy
import random

class Joss(Strategy):

    def __init__(self):
        self.player_number = None

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if not history:
            return 'c'

        # 90% of the time, copy the opponents last move
        if random.random() < 0.9:
            opponent_last_move = history[-1][1] if self.player_number == 1 else history[-1][0]
            return opponent_last_move

        # 10% of the time, defect
        return 'd'

    def get_name(self):
        return 'Joss'
