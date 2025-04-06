from brain_games.games.progression_game import progression_game
from brain_games.module import game_run

QUESTION = "What number is missing in the progression?"


def main():
    game_run(QUESTION, progression_game)


if __name__ == "__main__":
    main()
