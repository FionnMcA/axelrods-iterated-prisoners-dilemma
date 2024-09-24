from strategy import Strategy


class Friedman(Strategy):
    """
        Cooperates but once the opponent defects, it will only defect
    """

    def __init__(self):
        self.player_number = None
        self.grudge = False

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if not history:
            return 'c'

        opponent_last_move = history[-1][1] if self.player_number == 1 else history[-1][0]

        if opponent_last_move == 'd':
            self.grudge = True

        if self.grudge:
            return 'd'

        return 'c'

    def get_name(self):
        return "Friedman"
