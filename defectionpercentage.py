import random

from strategy import Strategy


class DefectionPercentage(Strategy):
    """
        Monitor the opponent's first 10 moves to determine the frequency of defections.
        Calculate the percentage of rounds in which the opponent defected.
        After the first 10 rounds, defect with the same probability as the opponent's defection rate,
        maintaining this probabilistic behavior for the remainder of the game.
    """

    def __init__(self):
        self.player_number = None
        self.defection_percentage = 0
        self.defection_count = 0

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if not history:
            return 'c'

        if len(history) < 10:
            opponent_last_move = history[-1][1] if self.player_number == 1 else history[-1][0]
            if opponent_last_move == 'd':
                self.defection_count += 1
            return 'c'

        if len(history) == 10:
            self.defection_percentage = self.defection_count / 10

        if random.random() < self.defection_percentage:
            return 'd'
        return 'c'

    def get_name(self):
        return 'Defection Percentage'
