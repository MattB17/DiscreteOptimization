#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Used to define methods for solving the knapsack problem.

"""
def backtrack(n, capacity, dp, weights):
    curr_capacity = capacity
    curr_item = n
    taken = ["0" for _ in range(n)]
    while (curr_capacity > 0 and curr_item > 0):
        if (dp[curr_capacity][curr_item] != dp[curr_capacity][curr_item-1]):
            taken[curr_item - 1] = "1"
            curr_capacity -= weights[curr_item - 1]
        curr_item -= 1
    return taken

def run_dp_knapsack(values, weights, capacity, n):
    dp = [[0 for _ in range(n+1)] for _ in range(capacity+1)]
    for k in range(1, capacity+1):
        for j in range(1, n+1):
            dp[k][j] = dp[k][j-1]
            if weights[j-1] <= k:
                add_item_val = dp[k - weights[j-1]][j-1] + values[j-1]
                dp[k][j] = max(dp[k][j], add_item_val)
    return dp

def dp_solver(values, weights, capacity):
    n = len(values)
    dp = run_dp_knapsack(values, weights, capacity, n)
    taken = backtrack(n, capacity, dp, weights)
    return "{0} 1\n{1}".format(dp[capacity][n], " ".join(taken))
