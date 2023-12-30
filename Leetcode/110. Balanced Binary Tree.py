"""
Given a binary tree, determine if it is height-balanced

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every 
node never differs by more than one.

Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Input: root = []
Output: true

Approach:
-We can check the depth of each subtree of any given node but finding the longest path at each child node
-Compare left and right to ensure that the difference is <= 1

"""
class Tree:
    def __init__(self) -> None:
        pass

    def depth(self, root):
        if root is None:
            return 0
        
        left = self.depth(root.left) if root.left else 0
        right = self.depth(root.right) if root.right else 0

        return 1 + max(left, right)

    def height_balanced(self,root):
        # Base case: if root is None return True
        if root is None:
            return True
        
        # Find the longest path of each child node
        left = self.depth(root.left)
        right = self.depth(root.right)

        # Compare left and right
        # Return true if difference of left and right <= 1
        if abs(left - right) <= 1 and self.height_balanced(root.left) and self.height_balanced(root.right):
            return True
        return False

