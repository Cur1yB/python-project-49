#!/usr/bin/env python3
from brain_games.games.calc_game import calc_game
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    calc_game(name)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
