from strategy import Strategy


class ZigZag(Strategy):
    """
        Starts by cooperating then cooperates and defects every second move
    """


    def player_move(self, history):
        if not history:
            return 'c'

        return 'c' if len(history) % 2 == 0 else 'd'

    def get_name(self):
        return 'Zig Zag'