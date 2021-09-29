#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def knapsack_solver(items, capacity):
    total_value = 0
    n = len(items)
    taken = ["0" for _ in range(n)]
    for i in range(n):
        if items[i].weight <= capacity:
            taken[i] = "1"
            capacity -= items[i].weight
            total_value += items[i].value
    return "{0} 0\n{1}".format(total_value, " ".join(taken))



def solve_it(input_data):
    lines = input_data.split('\n')
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    items = [None for _ in range(item_count)]
    for i in range(item_count):
        line = lines[i+1].split()
        items[i] = Item(int(line[0]), int(line[1]))
    return knapsack_solver(items, capacity)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print("This test requires an input file. " +
              "Please select one from the data directory. " +
              "(i.e. python solver.py ./data/ks_4_0)")
