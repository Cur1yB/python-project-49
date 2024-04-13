#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.calc_game import calc_game


QUESTION = 'What is the result of the expression?'


def main():
    run_game(calc_game, QUESTION)


if __name__ == '__main__':
    main()
