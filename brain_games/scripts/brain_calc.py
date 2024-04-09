#!/usr/bin/env python3
import prompt
import random
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        random_int_1 = random.randint(1, 10)
        random_int_2 = random.randint(1, 10)
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
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
