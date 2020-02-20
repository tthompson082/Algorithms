#!/usr/bin/python
# for 1: [['rock'], ['paper'], ['scissors']]
# for 2: [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
# for 3: [[r,r,r], [r,r,p], [r,r,s], [r,p,r], [r,p,p], [r,p,s], [r,s,r], [r,s,p], [r,s,s], [p,r,r], [p,r,p], [p,r,s], [p,p,r], [p,p,p], [p,p,s], [p,s,r], [p,s,p], [p,s,s], [s,r,r], [s,r,p], [s,r,s], [s,p,r], [s,p,p], [s,p,s], [s,s,r], [s,s,p], [s,s,s]]

import sys


def rock_paper_scissors(n):
    rps_plays = ['rock', 'paper', 'scissors']
    possible_combinations = []
    if n < 0:
        return 0
    elif n == 0:
        return [[]]
    else:
        def inner_function(play):
            if len(play) == n:
                possible_combinations.append(play)
            else:
                for i in range(len(rps_plays)):
                    value = play + [rps_plays[i]]
                    inner_function(value)
        inner_function([])
    return possible_combinations


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
