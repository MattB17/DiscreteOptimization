"""
This module implements the `BranchNode` class which is a class used to denote
a node in the branch and bound algorithm for the knapsack problem.

"""
from collections import namedtuple

BranchNode = namedtuple("BranchNode",
                        ["items", "last_item", "cap", "val", "max_val"])
