from strategy import Strategy


class TwoTitsForTat(Strategy):
    """
        if the opponent defects once, then retaliate by defecting 2 times
    """

    def __init__(self):
        self.player_number = None
        self.defect_count = 0

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        if history:
            opponent_last_move = history[-1][1] if self.player_number == 1 else history[-1][0]

            if opponent_last_move == 'd':
                self.defect_count += 1

            if self.defect_count > 0:
                self.defect_count -= 1
                return 'd'
        return 'c'

    def get_name(self):
        return 'Two Tits For Tat'
