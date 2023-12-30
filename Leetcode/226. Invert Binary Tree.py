"""
Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []

Approach:
-Brute force:
-Traverse down the tree and switch node.left and node.right until there are no more children
-Can be performed recursively or iteritively

"""
class TreeNode:
    def __init__(self, data, left=None, right=None ):
        self.data = data
        self.left = left
        self.right = right


def invert_tree(node):
    # Base case: 
    # If node is None then return
    if node is None:
        return

    # Swap the left and right nodes and recurse
    temp = node.left
    node.left = node.right
    node.right = temp
    invert_tree(node.left)
    invert_tree(node.right)

