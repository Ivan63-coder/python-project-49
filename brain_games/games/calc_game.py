import operator
import random


def calc_game():
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul}
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    op = random.choice(list(ops.keys()))
    question = f'{num1} {op} {num2}'

    correct_answer = str(ops[op](num1, num2))
    
    return question, correct_answer
