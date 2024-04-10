import prompt
import random

MAX_ROUNDS = 3
MIN_NUMBER = 1
MAX_NUMBER = 100


def prime_game(name):
    count = 0
    while count < MAX_ROUNDS:
        random_int = random.randint(MIN_NUMBER, MAX_NUMBER)
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


def is_prime(n):
    """Проверяет, является ли число n простым."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
