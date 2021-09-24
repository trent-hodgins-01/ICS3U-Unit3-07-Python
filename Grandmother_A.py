# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/24/2021
# This is the GrandmotherA program
# The user enters in their age and the program tells them if they can date their grandchild


import random


def main():
    # this function checks to see if the user is allowed to date her grandchild

    # input
    age_as_string = input("Enter in your age: ")
    print("")

    # process and output
    try:
        age_as_number = int(age_as_string)
        if age_as_number >= 25 and age_as_number <= 40:
            print("you are allowed to date my grandchild.")
        elif age_as_number < 25:
            print("You are too young.")
        elif age_as_number > 40:
            print("You are too old")

    except Exception:
        print("You didn’t enter in a number.")

    print("\nDone")


if __name__ == "__main__":
    main()
