from brain_games.games.even_game import even_game
from brain_games.module import game_run

QUESTION = "Answer 'yes' if the number is even, otherwise answer 'no'."


def main():
    game_run(QUESTION, even_game)


if __name__ == "__main__":
    main()
