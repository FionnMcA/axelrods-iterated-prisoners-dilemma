from strategy import Strategy


class Grofman(Strategy):
    """
        Responds based on the opponent's behavior over the last 7 moves.
        The strategy cooperates by default but can enter a "grudge mode" if the opponent defects often
    """

    def __init__(self):
        self.player_number = None
        self.grudge = False

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if len(history) < 2:
            return 'c'

        if self.grudge:
            return 'd'

        opponent_last_move = history[-1][1] if self.player_number == 1 else history[-1][0]

        if len(history) % 7 != 0:
            return opponent_last_move

        opponent_last_seven_moves = [move[1] if self.player_number == 1 else move[0] for move in history[-7:]]

        if opponent_last_seven_moves.count('d') >= 3 or (
                opponent_last_seven_moves.count('d') == 2 and opponent_last_move == 'd'):
            self.grudge = True
            return 'd'

        return 'c'

    def get_name(self):
        return 'Grofman'
