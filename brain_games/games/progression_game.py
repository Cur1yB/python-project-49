import prompt
import random
from brain_games.scripts.congratulations import congratulations

MAX_ROUNDS = 3
MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 5
MIN_START_NUMBER = 1
MAX_START_NUMBER = 10


def progression_game(name):
    count = 0
    while count < MAX_ROUNDS:
        progression, result = generate_progression()
        print(f'Question: {progression}')
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


def generate_progression():
    start = random.randint(MIN_START_NUMBER, MAX_START_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = [start + step * i for i in range(length)]
    gap_index = random.randint(0, length - 1)
    result = progression[gap_index]
    progression[gap_index] = ".."
    progression_str = ' '.join(str(x) for x in progression)
    return progression_str, result
