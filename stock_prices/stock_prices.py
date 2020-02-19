#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_min_price_so_far = None
    max_profit_so_far = None
    for i in range(len(prices)):
        if i == 0:
            current_min_price_so_far = prices[i]
        if i == 1:
            if prices[i] < current_min_price_so_far:
                current_min_price_so_far = prices[i]
            max_profit_so_far = prices[i] - prices[i-1]
        if i > 1:
            if prices[i] < current_min_price_so_far:
                current_min_price_so_far = prices[i]
            for j in range(i-1, 0, -1):
                if prices[i]-prices[j] > max_profit_so_far:
                    max_profit_so_far = prices[i]-prices[j]
    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
