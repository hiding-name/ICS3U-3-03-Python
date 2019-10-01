#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program adds numbers

import random


def main():
    # funciton makes user guess nimber

    # variables
    number = random.randint(1, 101)

    # input
    guess = float(input("Guess the number: "))

    # process
    if guess == number:
        # output
        print("Good job, you got it.")
    else:
        print("you got it wrong.")


if __name__ == "__main__":
    main()
