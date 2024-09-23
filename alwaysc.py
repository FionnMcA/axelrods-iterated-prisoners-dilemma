from strategy import Strategy


class AlwaysC(Strategy):

    def player_move(self, history):
        return 'c'

    def get_name(self):
        return 'Always Cooperate'
