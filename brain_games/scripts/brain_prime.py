#!/usr/bin/env python3
from brain_games.games.prime_game import prime_game
from brain_games.engine import run_game


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_game(prime_game, QUESTION)


if __name__ == '__main__':
    main()
