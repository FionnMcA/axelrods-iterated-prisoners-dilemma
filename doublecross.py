from strategy import Strategy


class DoubleCross(Strategy):

    def player_move(self, history):
        if len(history) < 50:
            return 'c'
        return 'd'

    def get_name(self):
        return 'Double Cross'