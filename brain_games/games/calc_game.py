import prompt
import random
from brain_games.scripts.congratulations import congratulations

MAX_ROUNDS = 3
MIN_NUMBER = 1
MAX_NUMBER = 10


def calc_game(name):
    count = 0
    while count < MAX_ROUNDS:
        random_int_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_int_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        action = random.choice(['*', '+', '-'])
        operation = ' '.join((str(random_int_1), action, str(random_int_2)))
        result = int(eval(operation))
        print(f'Question: {operation}')
        answer = prompt.integer('Your answer: ')
        if answer == result:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  + f" Correct answer was '{result}'. \n"
                  + f"Let's try again, {name}!")
            break
    congratulations(count, MAX_ROUNDS, name)
