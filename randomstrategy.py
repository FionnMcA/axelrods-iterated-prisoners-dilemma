import random
from strategy import Strategy


class RandomStrategy(Strategy):
    """
        Chooses its move randomly, with an equal chance of cooperating or defecting.
    """
    def player_move(self, history):
        return 'c' if random.random() < 0.5 else 'd'

    def get_name(self):
        return 'Random'
