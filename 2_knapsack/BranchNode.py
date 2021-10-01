"""
This module implements the `BranchNode` class which is a class used to denote
a node in the branch and bound algorithm for the knapsack problem.

"""

class BranchNode:
    def __init__(self, curr_items, last_item,
                 rem_capacity, curr_value, max_value):
        self.curr_items = curr_items
        self.last_item = last_item
        self.rem_capacity = rem_capacity
        self.curr_value = curr_value
        self.max_value = max_value

    def get_branch_item(self):
        return self.last_item + 1

    def __str__(self):
        return "------------\n{0}\n{1}\n{2}\n{3}\n{4}\n------------".format(
            self.curr_items, self.last_item, self.rem_capacity,
            self.curr_value, self.max_value)
