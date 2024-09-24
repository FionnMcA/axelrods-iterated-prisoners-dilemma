from strategy import Strategy


class TitForTwoTats(Strategy):

    def __init__(self):
        self.player_number = None

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if len(history) < 2:
            return 'c'

        if self.player_number == 1:
            last_two_moves = [move[1] for move in history[-2:]]
        else:
            last_two_moves = [move[0] for move in history[-2:]]

        if all(move == 'd' for move in last_two_moves):
            return 'd'

        return 'c'

    def get_name(self):
        return 'Tit For Two Tats'
