from strategy import Strategy

# Zig Zag but start by defecting
class ReverseZigZag(Strategy):

    def player_move(self, history):
        if not history:
            return 'd'

        return 'c' if len(history) % 2 == 0 else 'd'

    def get_name(self):
        return 'Reverse Zig Zag'