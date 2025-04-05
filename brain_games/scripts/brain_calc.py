from brain_games.games.calc_game import calc_game
from brain_games.module import game_run

QUESTION = "What is the result of the expression?"


def main():
    game_run(QUESTION, calc_game)


if __name__ == "__main__":
    main()
