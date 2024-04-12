import prompt
import random
from brain_games.scripts.congratulations import congratulations

MAX_ROUNDS = 3
MIN_NUMBER = 1
MAX_NUMBER = 100


def even_game(name):
    count = 0
    while count < MAX_ROUNDS:
        random_int = random.randint(MIN_NUMBER, MAX_NUMBER)
        print(f'Question: {random_int}')
        answer = prompt.string('Your answer: ')
        if random_int % 2 == 0 and answer == 'yes':
            print('Correct!')
            count += 1
        elif random_int % 2 == 1 and answer == 'no':
            print('Correct!')
            count += 1
        elif random_int % 2 == 1 and answer == 'yes':
            print("'yes' is wrong answer ;(."
                  + f" Correct answer was 'no'. \nLet's try again, {name}!")
            break
        else:
            print("'no' is wrong answer ;(."
                  + f" Correct answer was 'yes'. \nLet's try again, {name}!")
            break
    congratulations(count, MAX_ROUNDS, name)
