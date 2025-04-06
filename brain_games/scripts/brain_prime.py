from brain_games.games.prime_game import prime_game
from brain_games.module import game_run

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    game_run(QUESTION, prime_game)


if __name__ == "__main__":
    main()