import operator
import random

import prompt


def brain_games():
    print("Welcome to the Brain Games!")


def brain_even():
    brain_games()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    for _ in range(3):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input('Your answer: ').strip().lower()
        correct = 'yes' if number % 2 == 0 else 'no'

        if answer != correct:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")


def brain_calc():
    brain_games()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul}
    for _ in range(3):
        num1 = random.randint(1, 25)
        num2 = random.randint(1, 25)
        op = random.choice(list(ops.keys()))
        question = f'{num1} {op} {num2}'
        correct_answer = str(ops[op](num1, num2))
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
