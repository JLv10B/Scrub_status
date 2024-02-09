"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).\

Input:
                1
            2       2
        5     6   6      5

Output = True

Input:
                1
            2       2
        5          5

Output = False
"""
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def symmetric_tree(root):
    """
    
    -If root.left == root.right
    -Then look at root.left.left == root.right.right

    -Traverse down from the root to the child nodes to make sure they are mirrored
    -If they are, for the left child we go left and the right child we go right and compare
    -At this point we can recurse down the tree until we reach all nodes or there is a miss match
    """

    def helper(left, right):
        # Base case: if there are no child nodes
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.data == right.data:
            return helper(left.left, right.right) and helper(left.right, right.left)
        return False
    
    return helper(root.left, root.right)