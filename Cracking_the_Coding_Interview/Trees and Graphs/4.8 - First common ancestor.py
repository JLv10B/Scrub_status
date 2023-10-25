"""
Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree

example:
            1
    2               3
4       5       6       7

Input: 4, 5
Output: 2

Notes:
-Given that the input is the specific nodes we have to consider 2 senarios
-1.) The node is linked to it's parent, 2.) The node is not linked to it's parent
-If the node is linked to it's parent then we can traverse upwards until we find the first common ancestor
-If the node is not linked to it's parent then we can perform a depth first search to find each node then find the FCA

Approach 1:
-class Node (data, parent, left, right, depth) => linked to parent
-Compare depth of each node, if they are the same depth then we can traverse up the tree at the same rate
-If depth is different then we have to catch up the deeper node then traverse up the same rate
-When the depths are equal check if the nodes are not the same => first common ancestor
-If not continue to traverse until the nodes interesct
-If traversal ends and there is not intersection then the nodes are in different trees
"""
# Approach 1: Link to parent
class Node:
    def __init__(self, data, depth=0, parent=None, left=None, right=None):
        self.data = data
        self.depth = depth
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.data}'
         
def first_common_ancestor(node1, node2):
    while node1.depth != node2.depth:
        print(f'Node1 depth: {node1.depth}, Node2 depth: {node2.depth}')
        if node1.depth > node2.depth:
            node1 = node1.parent
        else:
            node2 = node2.parent
    
    if node1 == node2:
        return(f'First common ancestor: {node1}')
    else:
        while node1.parent and node2.parent:
            if node1.parent != node2.parent:
                node1 = node1.parent
                node2 = node2.parent
                # print(f'Node1: {node1}, Node2: {node2}')
            else:
                return(f'First common ancestor: {node1.parent}')
    return('Nodes are in different trees')
        
"""
Approach 2:
-class Node(data, left, right) => no link to parent
-Create a function that determines if the current node is one of the target nodes
-If true then return the current node
-If not then recurse for the left and right nodes
-If the left and right nodes contain one of the target notes then return the current node
-If only one of the child nodes contain one of the target nodes then return that child node

"""  
def first_ancestor(root, node1, node2):
    # Base case
    if root is None:
        return None
    
    # If node1 or node 2 is found then return the root node
    if root == node1 or root == node2:
        return root
    
    # left_fca and right_fca check if the left and right descendents include the target nodes
    left_fca = first_ancestor(root.left, node1, node2) 
    right_fca = first_ancestor(root.right, node1, node2)

    # If left_fca and right_fca are true then the root node's decendents include the target nodes
    if left_fca and right_fca:
        return root
    
    # If either left_fca or right_fca are none then the desendents only include one of the target nodes
    # Return the side that is not None to continue looking up the tree to find the first common ancenstor
    if left_fca is None:
        return right_fca 
    else:
        return left_fca

def nodes_found(root, node1, node2):
    first_node = False
    second_node = False
    queue = [root]
    visited = []

    while queue:
        if first_node is False or second_node is False:
            current_node = queue.pop(0)
            if current_node == node1:
                first_node = True
            elif current_node == node2:
                second_node = True
            if current_node.left and current_node.left not in visited:
                queue.append(current_node.left)
            if current_node.right and current_node.right not in visited:
                queue.append(current_node.right)
            visited.append(current_node)
        else:
            return first_ancestor(root, node1, node2)
    
    return('Nodes are in different trees')
    

# Testing:

# node = Node(1)
# node.left = Node(2, 1, node)
# node.right = Node(3,1, node)
# node.left.left = Node(4,2, node.left)
# node.left.right = Node(5,2, node.left)
# node.right.left = Node(6,2, node.right)
# node.right.right = Node(7,2, node.right)
# node2 = Node(17)

# print(first_common_ancestor(node.left.left, node.left))

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.right = Node(7)
node2 = Node(17)

print(nodes_found(node, node.right, node.right.left))