#!/usr/bin/env python3
from brain_games.games.gcd_game import gcd_game
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    gcd_game(name)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
