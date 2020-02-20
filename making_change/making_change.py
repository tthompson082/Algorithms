#!/usr/bin/python
# can use pennies, nickels, dimes, quarters, and half-dollars: [1, 5, 10, 25, 50]
# For 0 there are 0 ways
# For 1: 1 penny
# For 2: 1 penny 1 penny
# For 3: 1 penny 1 penny 1 penny
# for 4: 1 penny 1 penny 1 penny 1 penny
# for 5: 1 penny 1 penny 1 penny 1 penny 1 penny
# for 5: 1 nickel
# for 6: 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny
# for 6: 1 nickel 1 penny
# for 7: 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny
# for 7: 1 nickel 1 penny 1 penny
# for 8: 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny
# for 8: 1 nickel 1 penny 1 penny 1 penny
# for 9: 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny
# for 9: 1 nickel 1 penny 1 penny 1 penny 1 penny
# for 10: 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny 1 penny
# for 10: 1 nickel 1 penny 1 penny 1 penny 1 penny 1 penny
# for 10: 1 nickel 1 nickel
# for 10: 1 dime

import sys


def making_change(amount, denominations):
    pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
