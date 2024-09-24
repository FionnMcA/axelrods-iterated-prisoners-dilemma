from strategy import Strategy


class TitForThreeTats(Strategy):

    def __init__(self):
        self.player_number = None

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if len(history) < 3:
            return 'c'

        opponent_last_three_moves = [move[1] if self.player_number == 1 else move[0] for move in history[-3:]]

        if all(move == 'd' for move in opponent_last_three_moves):
            return 'd'
        return 'c'

    def get_name(self):
        return 'Tit For Three Tats'