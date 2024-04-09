#!/usr/bin/env python3
import prompt
import random
from brain_games.cli import welcome_user


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(5, 10)
    progression = [start + step * i for i in range(length)]
    gap_index = random.randint(0, length - 1)
    result = progression[gap_index]
    progression[gap_index] = "..."
    progression_str = ' '.join(str(x) for x in progression)
    return progression_str, result


def main():
    name = welcome_user()
    count = 0
    while count < 3:
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
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
