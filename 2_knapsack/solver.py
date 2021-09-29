#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def knapsack_solver(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(n + 1)] for _ in range(capacity + 1)]
    for k in range(1, capacity + 1):
        for i in range(1, n+1):
            dp[k][i] = dp[k][i-1]
            if weights[i-1] <= k:
                add_item_val = dp[k - weights[i-1]][i-1] + values[i-1]
                dp[k][i] = max(dp[k][i], add_item_val)

    total_val = dp[capacity][n]
    taken = ["0" for _ in range(n)]
    while (capacity > 0  and n > 0):
        if (dp[capacity][n] != dp[capacity][n-1]):
            taken[n-1] = "1"
            capacity -= weights[n-1]
        n -= 1

    return "{0} 1\n{1}".format(total_val, " ".join(taken))


def solve_it(input_data):
    lines = input_data.split('\n')
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    values = [None for _ in range(item_count)]
    weights = [None for _ in range(item_count)]
    for i in range(item_count):
        line = lines[i+1].split()
        values[i] = int(line[0])
        weights[i] = int(line[1])
    return knapsack_solver(values, weights, capacity)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
