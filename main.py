from itertools import combinations
from titfortat import TitForTat
from alwaysc import AlwaysC
from alwaysd import AlwaysD
from prisonersdilemma import PrisonersDilemma


def play_all_strategies():
    strategies = [
        AlwaysC(),
        AlwaysD(),
        TitForTat()
    ]

    for strategy1, strategy2 in combinations(strategies, 2):
        if hasattr(strategy1, 'set_player_number'):
            strategy1.set_player_number(1)
        if hasattr(strategy2, 'set_player_number'):
            strategy2.set_player_number(2)

        prisoner_dilemma = PrisonersDilemma(strategy1, strategy2, 10)
        prisoner_dilemma.play_game()


if __name__ == '__main__':
    play_all_strategies()
