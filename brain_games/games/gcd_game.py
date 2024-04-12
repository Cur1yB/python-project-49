import prompt
import random
from brain_games.scripts.congratulations import congratulations

MAX_ROUNDS = 3
MIN_NUMBER = 1
MAX_NUMBER = 100


def gcd_game(name):
    count = 0
    while count < MAX_ROUNDS:
        random_int_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_int_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        print('Question:', random_int_1, random_int_2)
        result = gcd(random_int_1, random_int_2)
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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
