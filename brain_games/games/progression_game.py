import random


def progression_game():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = [start + i * step for i in range(length)]

    index = random.randint(0, length - 1)
    correct_answer = progression[index]
    progression[index] = '..'

    question = " ".join(map(str, progression))
    
    return question, correct_answer
