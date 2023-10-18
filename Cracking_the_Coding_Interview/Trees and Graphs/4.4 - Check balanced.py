"""
Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one

Notes:
-Breadth first traversal
-Balanced tree means the all the nodes of the same depth must have no more than 1 depth difference
-In order to find if there is > 1 depth difference we can compare the depths of each leaf on the tree

"""

# Tree node class - data, left, right
class BinaryNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Initiate [queue] with (node, depth) for root, [visited], max_depth and min_depth to hold depth values
# while queue has values
# If node does not have child nodes, this means it's a leaf, compare leaf depth to max_depth and min_depth
# If node has child node(s) add to queue
def check_balanced(root):
    if root is None:
        return('No Tree!')
    
    queue = [(root,0)]
    visited = []
    max_depth = 0
    min_depth = None
    while queue:
        current_node, current_depth = queue.pop(0)
        if current_node.left is None and current_node.right is None:
            if current_depth > max_depth:
                max_depth = current_depth
            if min_depth is None:
                min_depth = current_depth
            elif current_depth < min_depth:
                min_depth = current_depth
        else:
            if current_node.left and current_node.left not in visited:
                queue.append((current_node.left, current_depth +1))
                visited.append(current_node.left)
            if current_node.right and current_node.right not in visited:
                queue.append((current_node.right, current_depth +1))
                visited.append(current_node.right)
        # print(f'Min depth: {min_depth}, Max depth: {max_depth}')

    depth_difference = max_depth - min_depth

    if depth_difference >1:
        return(f'Difference in depth is: {depth_difference}. This is a unbalanced binary tree')
    else:
        return(f'Difference in depth is: {depth_difference}. This is an balanced binary tree')
    
# Testing:
if __name__ == '__main__':
    # root = BinaryNode(1)
    # root.left = BinaryNode(2)
    # root.left.left = BinaryNode(4)
    # root.left.right = BinaryNode(5)
    # root.left.right.right = BinaryNode(6)
    # root.left.right.right.right = BinaryNode(7)
    # root.right = BinaryNode(3)
    # root.right.left = BinaryNode(8)
    # root.right.right = BinaryNode(9)
    # root.right.right.right = BinaryNode(10)
    # root.right.right.right.right = BinaryNode(11)

    root = BinaryNode(7)
    root.left = BinaryNode(2)
    root.left.left = BinaryNode(4)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)

    print(check_balanced(root))