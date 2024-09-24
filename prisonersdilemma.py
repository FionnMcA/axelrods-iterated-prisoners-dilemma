import csv


class PrisonersDilemma:
    # The tuple represents the moves ('c' for cooperate, 'd' for defect) and the resulting points for Player 1 and
    # Player 2.
    outputs = {
        ('c', 'c'): (3, 3),  # Both cooperate: each gets 3 points.
        ('c', 'd'): (0, 5),  # Player 1 cooperates, Player 2 defects: Player 1 gets 0, Player 2 gets 5.
        ('d', 'c'): (5, 0),  # Player 1 defects, Player 2 cooperates: Player 1 gets 5, Player 2 gets 0.
        ('d', 'd'): (1, 1)  # Both defect: each gets 1 point.
    }

    def __init__(self, strategy1, strategy2, rounds):
        """
            Initializes the Prisoner's Dilemma game with two strategies and the number of rounds.

            Parameters:
            strategy1: The first strategy (Player 1).
            strategy2: The second strategy (Player 2).
            rounds: The number of rounds to play (random between 250 and 500)
        """
        self.strategy1 = strategy1
        self.strategy2 = strategy2
        self.rounds = rounds
        self.history = []
        self.p1_points = 0
        self.p2_points = 0

    def play_round(self):
        move1 = self.strategy1.player_move(self.history)
        move2 = self.strategy2.player_move(self.history)
        self.history.append((move1, move2))
        points1, points2 = self.outputs.get((move1, move2))
        self.p1_points += points1
        self.p2_points += points2

        return {''.ljust(50): '', 'Player 1'.ljust(40): move1, 'Player 2'.ljust(40): move2}

    def play_game(self):
        """
            Plays the entire game for the specified number of rounds and writes the results to a CSV file.

            Returns:
            The total points for Player 1 and Player 2 after all rounds.
        """

        with open('axelrod-tournament-results.csv', mode='a', newline='') as csvfile:
            fieldnames = [''.ljust(50), 'Player 1'.ljust(40),
                          'Player 2'.ljust(40)]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            game_header = {
                ''.ljust(50): ''.ljust(40),
                'Player 1'.ljust(40): self.strategy1.get_name().ljust(40),
                'Player 2'.ljust(40): self.strategy2.get_name().ljust(40)
            }
            writer.writerow(game_header)

            for _ in range(self.rounds):
                move_data = self.play_round()
                writer.writerow(move_data)

            totals_data = {
                'Total': 'Total',
                'Player 1': self.p1_points,
                'Player 2': self.p2_points
            }

            fieldnames = ['Total', 'Player 1', 'Player 2']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(totals_data)
            csvfile.write('\n')

        return self.p1_points, self.p2_points
