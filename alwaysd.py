from strategy import Strategy


class AlwaysD(Strategy):

    def player_move(self, history):
        return 'd'

    def get_name(self):
        return 'Always Defect'
