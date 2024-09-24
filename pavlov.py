from strategy import Strategy


class Pavlov(Strategy):

    def __init__(self):
        self.player_number = None

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if not history:
            return 'c'

        own_last_move = history[-1][0] if self.player_number == 1 else history[-1][1]
        opponent_last_move = history[-1][1] if self.player_number == 2 else history[-1][0]

        # Win-Stay if last round was mutual cooperation or mutual defection
        if own_last_move == opponent_last_move:
            return own_last_move

        # Lose-Shift: if mismatched switch moves
        return 'd' if own_last_move == 'c' else 'c'

    def get_name(self):
        return 'Pavlov'
