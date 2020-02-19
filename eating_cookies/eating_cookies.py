#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, starting_position=0, cache={}):
    ways_to_eat_cookies = [1, 2, 3]
    how_many_possible_ways = 0
    if n < 0:
        return 0
    if n == 0:
        return 1
    computed_ways = {}
    for i in range(len(ways_to_eat_cookies)):
        if n - ways_to_eat_cookies[i] not in computed_ways:
            computed_ways[n - ways_to_eat_cookies[i]] = True
            how_many_possible_ways += eating_cookies(
                n - ways_to_eat_cookies[i], i, computed_ways)
    return how_many_possible_ways


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
