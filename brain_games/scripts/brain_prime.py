#!/usr/bin/env python3
from brain_games.games.prime_game import prime_game
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    prime_game(name)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
