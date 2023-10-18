"""
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent

ex.
Input:
    1
2       3
      4   5

output = [2,1,4,3,5]

Approach:
-In-order traversing lists the left node then the current node then the right node
-Any time you look at a node you need to look to see if there is a left child node before considering going to the 
    current node then the right node
-This sounds like recursion could would
-Base case if node does not have any child nodes then append to result and return

"""

# Normal tree node w/ link to it's parent
class TreeNode:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = left

result = []
def find_successor(root):
    if root is None:
        return None
    
    else:
        find_successor(root.left)
        result.append(root.data)
        find_successor(root.right)

    return result


# Testing:

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(find_successor(root))