import csv


class PrisonersDilemma:
    outputs = {
        ('c', 'c'): (3, 3),
        ('c', 'd'): (0, 5),
        ('d', 'c'): (5, 0),
        ('d', 'd'): (1, 1)
    }

    def __init__(self, strategy1, strategy2, rounds=10):
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
        print('Playing the game')
        with open('axelrod-tournament-results.csv', mode='a', newline='') as csvfile:
            fieldnames = [''.ljust(50), 'Player 1'.ljust(40),
                          'Player 2'.ljust(40)]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            game_header = {
                ''.ljust(50): '',
                'Player 1'.ljust(40): self.strategy1.get_name(),
                'Player 2'.ljust(40): self.strategy2.get_name()
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
