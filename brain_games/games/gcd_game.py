import prompt
import random


def gcd_game(name):
    count = 0
    while count < 3:
        random_int_1 = random.randint(1, 100)
        random_int_2 = random.randint(1, 100)
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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
