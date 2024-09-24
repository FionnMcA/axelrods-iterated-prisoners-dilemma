import csv
import random
from itertools import product
from titfortat import TitForTat
from alwaysc import AlwaysC
from alwaysd import AlwaysD
from randomstrategy import RandomStrategy
from prisonersdilemma import PrisonersDilemma
from supicioustitfortat import SuspiciousTitForTat
from titfortwotats import TitForTwoTats
from generoustitfortat import GenerousTitForTat
from friedman import Friedman
from joss import Joss
from graaskamp import Graaskamp
from grofman import Grofman
from doublecross import DoubleCross
from reversetitfortat import ReverseTitForTat
from pavlov import Pavlov
from exploiter import Exploiter
from detective import Detective
from zigzag import ZigZag
from reversezigzag import ReverseZigZag
from titforthreetats import TitForThreeTats
from twotitsfortat import TwoTitsForTat
from defectionpercentage import DefectionPercentage
from generoustitfortwotats import GenerousTitForTwoTats


def play_all_strategies():
    strategies = [
        AlwaysC(),
        AlwaysD(),
        TitForTat(),
        RandomStrategy(),
        SuspiciousTitForTat(),
        TitForTwoTats(),
        GenerousTitForTat(),
        Friedman(),
        Joss(),
        Graaskamp(),
        Grofman(),
        DoubleCross(),
        ReverseTitForTat(),
        Pavlov(),
        Exploiter(),
        Detective(),
        ZigZag(),
        ReverseZigZag(),
        TitForThreeTats(),
        TwoTitsForTat(),
        DefectionPercentage(),
        GenerousTitForTwoTats()
    ]

    # It's important that we don't know the number of rounds
    rounds = random.randint(250, 500)

    total_results = {
        strategy.get_name(): {
            'wins': 0,
            'total_points': 0,
            'games_played': 0
        }
        for strategy in strategies
    }

    for strategy1, strategy2 in product(strategies, repeat=2):
        if hasattr(strategy1, 'set_player_number'):
            strategy1.set_player_number(1)
        if hasattr(strategy2, 'set_player_number'):
            strategy2.set_player_number(2)

        prisoner_dilemma = PrisonersDilemma(strategy1, strategy2, rounds)
        p1_points, p2_points = prisoner_dilemma.play_game()

        total_results[strategy1.get_name()]['total_points'] += p1_points
        total_results[strategy1.get_name()]['games_played'] += 1
        total_results[strategy2.get_name()]['total_points'] += p2_points
        total_results[strategy2.get_name()]['games_played'] += 1

        if p1_points > p2_points:
            total_results[strategy1.get_name()]['wins'] += 1
        elif p2_points > p1_points:
            total_results[strategy2.get_name()]['wins'] += 1

    # Write the totals to the csv file
    header_written = False
    for strategy, data in total_results.items():
        avg_points = round(data['total_points'] / data['games_played'], 2)
        strategy_totals = {
            'Strategy': strategy,
            'Wins': data['wins'],
            'Average': avg_points
        }
        with open('axelrod-tournament-results.csv', mode='a', newline='') as csvfile:
            fieldnames = ['Strategy', 'Wins', 'Average']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not header_written:
                writer.writeheader()
                header_written = True

            writer.writerow(strategy_totals)


if __name__ == '__main__':
    play_all_strategies()
