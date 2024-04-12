#!/usr/bin/env python3
from brain_games.games.even_game import even_game
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game(name)


if __name__ == '__main__':
    main()
