from brain_games.games.gcd_game import gcd_game
from brain_games.module import game_run

QUESTION = "Find the greatest common divisor of given numbers."


def main():
    game_run(QUESTION, gcd_game)


if __name__ == "__main__":
    main()
