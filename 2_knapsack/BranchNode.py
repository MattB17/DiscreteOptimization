"""
This module implements the `BranchNode` class which is a class used to denote
a node in the branch and bound algorithm for the knapsack problem.

"""

class BranchNode:
    def __init__(self, curr_items, last_item, curr_value, max_value):
        self.curr_items = curr_items
        self.last_item = last_item
        self.curr_value = curr_value
        self.max_value = max_value

    def get_branch_item(self):
        return self._last_item + 1
