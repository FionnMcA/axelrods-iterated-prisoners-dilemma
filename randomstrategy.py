import random
from strategy import Strategy


class RandomStrategy(Strategy):
    def player_move(self, history):
        return 'c' if random.random() < 0.5 else 'd'

    def get_name(self):
        return 'Random'
