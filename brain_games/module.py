import random

import prompt


def brain_games():
    print('Welcome to the Brain Games!')


def brain_even():
    brain_games()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ').strip().lower()
        correct = 'yes' if number % 2 == 0 else 'no'

        if answer != correct:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
