from strategy import Strategy
import random


class GenerousTitForTwoTats(Strategy):
    """
        Tit for two tats with a 10% chance of forgiveness
    """

    def __init__(self):
        self.player_number = None

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if len(history) < 2:
            return 'c'

        opponent_last_two_moves = [move[1] if self.player_number == 1 else move[0] for move in history[-2:]]

        # If the opponent defected twice, retaliate 90% of the time
        if all(move == 'd' for move in opponent_last_two_moves) and random.random() < 0.9:
            return 'd'
        return 'c'

    def get_name(self):
        return 'Generous Tit For Two Tats'
