#!/usr/bin/env python3
import prompt
import random
from brain_games.cli import welcome_user


def is_prime(n):
    """Проверяет, является ли число n простым."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        random_int = random.randint(1, 99)
        print(f'Question: {random_int}')
        answer = prompt.string('Your answer: ')
        if answer == 'yes' and is_prime(random_int):
            print('Correct!')
            count += 1
        elif answer == 'no' and not is_prime(random_int):
            print('Correct!')
            count += 1
        else:
            print("'yes' is wrong answer ;(."
                  + f" Correct answer was 'no'. \nLet's try again, {name}!")


if __name__ == '__main__':
    main()
