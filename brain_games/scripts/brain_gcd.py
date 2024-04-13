#!/usr/bin/env python3
from brain_games.games.gcd_game import gcd_game
from brain_games.engine import run_game


QUESTION = 'Find the greatest common divisor of given numbers.'


def main():
    run_game(gcd_game, QUESTION)


if __name__ == '__main__':
    main()
