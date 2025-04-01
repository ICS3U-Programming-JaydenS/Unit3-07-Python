#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 28, 2025
# This programs is a number guessing game

import random


def main():

    # Get the users guess and what to do if they dont pick a valid number.

    try:
        user_age = input("How Old are you: ")
        user_age_as_int = int(user_age)

        if (user_age_as_int > 25) and (user_age_as_int < 40):
            print("You May date my grandaughter")
        # What happens when they are too old.
        elif user_age_as_int >= 40:
            print("Your too old!")
        # What happens they are too young.
        else:
            print("Your too young!")
    # What happens if they put a invalid number.
    except Exception:
        print((user_age), " is not a valid number!")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
