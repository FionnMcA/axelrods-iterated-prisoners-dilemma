from strategy import Strategy



class Detective(Strategy):
    """
       The Detective strategy starts by probing the opponent's behavior for the first 10 moves using a preset sequence
       of cooperation and defection. After the probing phase, it analyzes the opponent's behavior and adjusts accordingly.
    """

    def __init__(self):
        self.player_number = None
        self.probe = ['c', 'c', 'd', 'c', 'c', 'c', 'd', 'd', 'c', 'c']  # Probing sequence
        self.defect_count = 0
        self.consecutive_cooperations = 0
        self.aggressive_mode = False

    def set_player_number(self, player_number):
        self.player_number = player_number

    def player_move(self, history):
        # First 10 rounds: Probing phase
        if len(history) < 10:
            return self.probe[len(history)]

        # After probing, count opponent defections during the probe
        if len(history) == 10:
            opponent_moves = [move[1] if self.player_number == 1 else move[0] for move in history[-10:]]
            self.defect_count = opponent_moves.count('d')

        # Handle aggressive mode (when opponent defected 4+ times)
        if self.aggressive_mode:
            opponent_last_move = history[-1][1] if self.player_number == 1 else history[-1][0]

            # Count consecutive cooperations by the opponent
            if opponent_last_move == 'c':
                self.consecutive_cooperations += 1
            else:
                self.consecutive_cooperations = 0

            # Forgive if the opponent cooperated for 3 consecutive rounds
            if self.consecutive_cooperations >= 3:
                self.aggressive_mode = False  # Exit aggressive mode (forgive opponent)
                self.consecutive_cooperations = 0  # Reset cooperation count
                return 'c'  # Cooperate again

            return 'd'  # Remain in aggressive mode, defecting

        if self.defect_count == 1:  # Likely Tit for Two Tats or a forgiving strategy
            return 'c' if len(history) % 2 == 0 else 'd'
        elif 2 <= self.defect_count <= 3:  # Likely Tit for Tat or a similar variant
            return 'c'
        elif self.defect_count >= 4:  # Likely uncooperative opponent
            self.aggressive_mode = True  # Enter aggressive mode
            return 'd'

        # Default to cooperation
        return 'c'

    def get_name(self):
        return 'Detective'
