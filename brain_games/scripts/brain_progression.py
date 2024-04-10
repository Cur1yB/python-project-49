#!/usr/bin/env python3
from brain_games.games.progression_game import progression_game
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    progression_game(name)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
