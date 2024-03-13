"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

from collections import deque

def binary_tree_traversal_order(binary_tree_root):
    """
    This function accepts the root of a binary tree and returns a nested list containing the node values organized level from left to right.

    To use this function import deque from collections

    Approach:
    - Initialize result = []
    - Utilize a queue/FIFO to perform breadth first traversal through the tree
        - While traversing separate the nodes for each level prior to appending to result
    """

    result = []

    if binary_tree_root == None:
        return result

    queue = deque()
    queue.append(binary_tree_root)

    while queue:
        level = []
        size = len(queue)
        
        for i in range(size):
            current_node = queue.popleft()
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            level.append(current_node)

        result.append(level)

    return result

