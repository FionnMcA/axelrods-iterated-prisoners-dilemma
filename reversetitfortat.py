from strategy import Strategy


class ReverseTitForTat(Strategy):
    """
        Cooperates first then does the opposite of the opponent's last move
    """

    def __init__(self):
        self.player_number = None

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if not history:
            return 'd'

        opponent_last_move = history[-1][1] if self.player_number == 1 else history[-1][0]

        if opponent_last_move == 'd':
            return 'c'
        return 'd'

    def get_name(self):
        return 'Reverse Tit For Tat'