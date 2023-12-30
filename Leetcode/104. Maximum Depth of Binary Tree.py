"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node 
down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

Approach:
-Traverse tree through DFS or BFS
-Add up nodes as you traverse down
"""
def maxDepth_recurseDFS(self, root):
    # Tree traversal
    # Recurse through the tree adding 1 if the node exists and 0 if node is None
    # Base case: node is None, return 0
    # return 1 + max(left, right)
    if root is None:
        return 0
    
    left = maxDepth_recurseDFS(root.left)
    right = maxDepth_recurseDFS(root.right)
    return 1 + max(left, right)

def maxDepth_BFS(self, root):
    if root is None:
        return 0
    
    # Initiate level = 0 to track longest path
    # Initiate que = [root] for BFS
    # While there are nodes in que check each node for children and put them into the que
    # We want to search through each level one by one then increment level
    level = 0
    que = [root]
    while que:
        for i in range(len(que)):
            node = que.pop(0)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        level += 1
    return level

