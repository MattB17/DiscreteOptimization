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


def solve_fractional_knapsack(item_tups, cutoff, capacity, n):
    total_val = 0
    item_idx = 0
    while (capacity > 0 and item_idx < n):
        if (item_tups[item_idx][2] <= cutoff):
            item_idx += 1
            continue
        if item_tups[item_idx][1] <= capacity:
            capacity -= item_tups[item_idx][1]
            total_val += item_tups[item_idx][0]
        else:
            frac_taken = capacity / item_tups[item_idx][1]
            total_val += frac_taken * item_tups[item_idx][0]
            capacity = 0
        item_idx += 1
    return total_val

def filter_items(item_tuples, cutoff):
    return [item_tuple for item_tuple in item_tuples
            if item_tuple[2] > cutoff]

def initialize_branch_and_bound(item_tups, capacity, n):
    first_node = BranchNode(
        set(), -1, capacity, 0,
        solve_fractional_knapsack(item_tups, -1, capacity, n))
    return deque([first_node])

def branch_right(node, next_item, n, item_tups):
    max_val = node.val + solve_fractional_knapsack(
        item_tups, next_item, node.cap, n - next_item - 1)
    right_node = BranchNode(
        node.items, next_item, node.cap, node.val, max_val)
    return right_node

def branch_left(node, next_item, n, item_tups, values, weights):
    curr_items = node.items.union({next_item})
    rem_cap = node.cap - weights[next_item]
    curr_val = node.val + values[next_item]
    max_val = curr_val + solve_fractional_knapsack(
        item_tups, next_item, rem_cap, n - next_item - 1)
    left_node = BranchNode(curr_items, next_item, rem_cap, curr_val, max_val)
    return left_node

def branch_and_bound(values, weights, capacity):
    n = len(values)
    item_tups = [(values[i], weights[i], i) for i in range(n)]
    item_tups.sort(key=lambda item_tup: item_tup[0]/item_tup[1],
                   reverse=True)
    bb_stack = initialize_branch_and_bound(item_tups, capacity, n)
    curr_best = 0
    best_soln = set()
    while (bb_stack):
        curr_node = bb_stack.popleft()
        next_item = curr_node.last_item + 1
        if (curr_node.val > curr_best):
            curr_best = curr_node.val
            best_soln = curr_node.items
        if (curr_node.max_val > curr_best and next_item < n):
            bb_stack.appendleft(branch_right(
                curr_node, next_item, n, item_tups))
            if (weights[next_item] <= curr_node.cap):
                bb_stack.appendleft(branch_left(
                    curr_node, next_item, n, item_tups, values, weights))
    taken = ["0" for _ in range(n)]
    for item in best_soln:
        taken[item] = "1"
    return "{0} 1\n{1}".format(curr_best, " ".join(taken))
