#!/usr/bin/env python3
import prompt
import random
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        random_int = random.randint(1, 99)
        print(f'Question: {random_int}')
        answer = prompt.string('Your answer: ')
        if random_int % 2 == 0 and answer == 'yes':
            print('Correct!')
            count += 1
        elif random_int % 2 == 1 and answer == 'no':
            print('Correct!')
            count += 1
        else:
            print(f''''yes' is wrong answer ;(. Correct answer was 'no'.
                  Let's try again, {name}!''')
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
