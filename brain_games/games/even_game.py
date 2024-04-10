import prompt
import random

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
        else:
            print("'yes' is wrong answer ;(."
                  + f" Correct answer was 'no'. \nLet's try again, {name}!")
