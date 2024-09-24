from strategy import Strategy


class TitForTwoTats(Strategy):
    """
        only retaliate if the opponent defected 2 times in a row
    """

    def __init__(self):
        self.player_number = None

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if len(history) < 2:
            return 'c'

        if all((move[1] if self.player_number == 1 else move[0]) == 'd' for move in history[-2:]):
            return 'd'

        return 'c'

    def get_name(self):
        return 'Tit For Two Tats'
