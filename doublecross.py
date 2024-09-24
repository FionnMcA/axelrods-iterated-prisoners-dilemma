from strategy import Strategy


class DoubleCross(Strategy):
    """
        Cooperate for the first 50 rounds to gain the opponent's trust
        Then defect from there on
    """

    def player_move(self, history):
        if len(history) < 50:
            return 'c'
        return 'd'

    def get_name(self):
        return 'Double Cross'
