#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Sep 2021
# This program finds the average of 3 integers 0-100


def main():
    # This function finds the average of 3 integers 0-100
    average = 0

    # Input
    integer1 = int(input("Enter an integer (0-100): "))
    integer2 = int(input("Enter an integer (0-100): "))
    integer3 = int(input("Enter an integer (0-100): "))

    # Process
    the_sum = integer1 + integer2 + integer3
    average = the_sum / 3
    # Output
    print("The average is {0}".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
