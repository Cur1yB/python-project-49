import random


MIN_NUMBER = 1
MAX_NUMBER = 10


def calc_game():
    random_int_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_int_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    action = random.choice(['*', '+', '-'])
    operation = ' '.join((str(random_int_1), action, str(random_int_2)))
    result = int(eval(operation))
    return operation, result
