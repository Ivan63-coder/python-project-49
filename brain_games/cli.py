import prompt

from .module import brain_games


def welcome_user():
    brain_games()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
