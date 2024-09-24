from strategy import Strategy

class ReverseZigZag(Strategy):
    """
        Starts with a defect then cooperates and defects every second move
    """

    def player_move(self, history):
        if not history:
            return 'd'

        return 'c' if len(history) % 2 == 0 else 'd'

    def get_name(self):
        return 'Reverse Zig Zag'