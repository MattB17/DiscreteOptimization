#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Used to define methods for solving the knapsack problem.

"""
from BranchNode import BranchNode
from collections import deque

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


def solve_fractional_knapsack(values, weights, capacity, n):
    item_tups = [(values[i], weights[i]) for i in range(n)]
    item_tups.sort(key=lambda item_tup: item_tup[0]/item_tup[1],
                   reverse=True)
    total_val = 0
    item_idx = 0
    while (capacity > 0 and item_idx < n):
        if item_tups[item_idx][1] <= capacity:
            capacity -= item_tups[item_idx][1]
            total_val += item_tups[item_idx][0]
        else:
            frac_taken = capacity / item_tups[item_idx][1]
            total_val += frac_taken * item_tups[item_idx][0]
            capacity = 0
        item_idx += 1
    return total_val

def branch_and_bound(values, weights, capacity):
    n = len(values)
    bb_stack = deque([BranchNode(
        set(), -1, capacity, 0,
        solve_fractional_knapsack(values, weights, capacity, n))])
    curr_best = 0
    best_soln = set()
    while (bb_stack):
        curr_node = bb_stack.popleft()
        next_item = curr_node.get_branch_item()
        if (curr_node.curr_value > curr_best):
            curr_best = curr_node.curr_value
            best_soln = curr_node.curr_items
        if (curr_node.max_value > curr_best and next_item < n):
            bb_stack.appendleft(BranchNode(
                curr_node.curr_items, next_item, curr_node.rem_capacity,
                curr_node.curr_value, solve_fractional_knapsack(
                    values[next_item+1:], weights[next_item+1:],
                    curr_node.rem_capacity, n - next_item - 1)))
            if (weights[next_item] <= curr_node.rem_capacity):
                bb_stack.appendleft(BranchNode(
                    curr_node.curr_items.union({next_item}, next_item,
                    curr_node.rem_capacity - weights[next_item],
                    curr_node.curr_value + values[next_item],
                    solve_fractional_knapsack(
                        values[next_item+1:], weights[next_item+1:],
                        curr_node.rem_capacity - weights[next_item],
                        n - next_item - 1))))
    taken = ["0" for _ in range(n)]
    for item in best_soln:
        taken[item] = "1"
    return "{0} 1\n{1}".format(curr_best, " ".join(taken))
