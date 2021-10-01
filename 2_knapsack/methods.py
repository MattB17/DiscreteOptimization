#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Used to define methods for solving the knapsack problem.

"""
from BranchNode import BranchNode
from collections import deque
import specs
import numpy as np

def backtrack(dp, weights, capacity, n, offset):
    curr_capacity = capacity
    curr_item = n
    taken_items = set()
    while (curr_capacity > 0 and curr_item > offset):
        i = curr_item - offset
        if (dp[curr_capacity][i] != dp[curr_capacity][i-1]):
            taken_items.add(curr_item - 1)
            curr_capacity -= weights[curr_item - 1]
        curr_item -= 1
    return dp[capacity][n-offset], taken_items


def run_dp_knapsack(values, weights, capacity, n, offset):
    dp = [[0 for _ in range(n+1 - offset)] for _ in range(capacity+1)]
    for k in range(1, capacity+1):
        for j in range(offset+1, n+1):
            i = j - offset
            dp[k][i] = dp[k][i-1]
            if weights[j-1] <= k:
                add_item_val = dp[k - weights[j-1]][i-1] + values[j-1]
                dp[k][i] = max(dp[k][i], add_item_val)
    return dp

def stringify(solution, n):
    taken = ["0" for _ in range(n)]
    for item in solution:
        taken[item] = "1"
    return taken

def dp_solver(values, weights, capacity):
    n = len(values)
    dp = run_dp_knapsack(values, weights, capacity, n, 0)
    opt, solution = backtrack(dp, weights, capacity, n, 0)
    return "{0} 1\n{1}".format(opt, " ".join(stringify(solution, n)))


def solve_fractional_knapsack(item_tups, offset, capacity, n):
    total_val = 0
    item_idx = 0
    while (capacity > 0 and item_idx < n):
        if (item_tups[item_idx][2] >= offset):
            if item_tups[item_idx][1] <= capacity:
                capacity -= item_tups[item_idx][1]
                total_val += item_tups[item_idx][0]
            else:
                frac_taken = capacity / item_tups[item_idx][1]
                total_val += frac_taken * item_tups[item_idx][0]
                capacity = 0
        item_idx += 1
    return total_val

def initialize_branch_and_bound(item_tups, capacity, n):
    first_node = BranchNode(
        set(), -1, capacity, 0,
        solve_fractional_knapsack(item_tups, 0, capacity, n))
    return deque([first_node])

def branch_right(node, next_item, n, item_tups):
    max_val = int(node.val + solve_fractional_knapsack(
        item_tups, next_item + 1, node.cap, n))
    right_node = BranchNode(
        node.items, next_item, node.cap, node.val, max_val)
    return right_node

def branch_left(node, next_item, n, item_tups, values, weights):
    curr_items = node.items.union({next_item})
    rem_cap = node.cap - weights[next_item]
    curr_val = node.val + values[next_item]
    max_val = int(curr_val + solve_fractional_knapsack(
        item_tups, next_item + 1, rem_cap, n))
    left_node = BranchNode(curr_items, next_item, rem_cap, curr_val, max_val)
    return left_node

def solve_directly(node, n):
    return ((n <= specs.DP_MAX_NODES) and
            ((n - node.last_item - 1) * node.cap) <= specs.DP_MAX_SIZE)

def solve_from_node(node, values, weights, n):
    offset = node.last_item + 1
    dp_soln = run_dp_knapsack(values, weights, node.cap, n, offset)
    opt, soln = backtrack(dp_soln, weights, node.cap, n, offset)
    return node.val + opt, node.items.union(soln)

def scale_inputs(capacity, weights, item_count):
    gcd = get_gcd(capacity, weights)
    if (gcd > 1):
        capacity = capacity // gcd
        for i in range(item_count):
            weights[i] = weights[i] // gcd
    return capacity, weights

def get_gcd(capacity, weights):
    curr_gcd = capacity
    for weight in weights:
        curr_gcd = gcd(weight, curr_gcd)
    return curr_gcd

def gcd(a, b):
    if (b == 0):
        return a
    new_a = a % b
    return gcd(b, new_a)

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
            if (solve_directly(curr_node, n)):
                val, soln = solve_from_node(curr_node, values, weights, n)
                if (val > curr_best):
                    curr_best = val
                    best_soln = soln
            else:
                bb_stack.appendleft(branch_right(
                    curr_node, next_item, n, item_tups))
                if (weights[next_item] <= curr_node.cap):
                    bb_stack.appendleft(branch_left(
                        curr_node, next_item, n, item_tups, values, weights))
    return "{0} 1\n{1}".format(curr_best, " ".join(stringify(best_soln, n)))
