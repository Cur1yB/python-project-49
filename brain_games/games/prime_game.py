import random


MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_game():
    random_int = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(random_int) else 'no'
    return random_int, correct_answer
