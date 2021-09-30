#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import methods


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
    return methods.dp_solver(values, weights, capacity)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
