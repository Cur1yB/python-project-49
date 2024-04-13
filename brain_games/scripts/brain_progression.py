#!/usr/bin/env python3
from brain_games.games.progression_game import progression_game
from brain_games.engine import run_game


QUESTION = 'What number is missing in the progression?'


def main():
    run_game(progression_game, QUESTION)


if __name__ == '__main__':
    main()
