"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3

Input: root = [1,2]
Output: 1

Approach:
-The diameter at any given node can be calculated by taking the longest path starting at each child node and
incrementing by 2 assuming there are 2 child nodes
-If a tree has 0 or 1 node then diameter is 0 because there are no edges
-We can use recursion to calcualte the diameter at each node and return the longest diameter of the tree

"""
class Tree:
    def __init__(self):
        self.diameter = 0
        
    def longest_path(self, root):
        # left = longest path of left child
        # right = longest path of right child
        
        left = self.diameter(root.left) if root.left else 0
        right = self.diameter(root.right) if root.right else 0
        diameter = left + right

        # Compare to self.diameter and return larger value
        if self.diameter < diameter:
            self.diameter = diameter

        # return longest path starting at root
        return 1 + max(left, right)
    
    def diameter(self, root):
        self.longest_path(root)
        return self.diameter

