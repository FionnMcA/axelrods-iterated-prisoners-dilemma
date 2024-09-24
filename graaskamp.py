from strategy import Strategy


class Graaskamp(Strategy):
    """
        Tit for tat but every 25 rounds defect - sneaky
    """

    def __init__(self):
        self.player_number = None

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if not history:
            return 'c'

        if len(history) % 25 == 24:
            return 'd'

        opponent_last_move = history[-1][1] if self.player_number == 1 else history[-1][0]
        return opponent_last_move

    def get_name(self):
        return 'Graaskamp'
