import random


MIN_NUMBER = 1
MAX_NUMBER = 100


def even_game():
    random_int = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if random_int % 2 == 0 else 'no'
    return random_int, correct_answer
