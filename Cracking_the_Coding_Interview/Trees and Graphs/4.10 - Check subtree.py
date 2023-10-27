"""
T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.

Notes:
-First thought is to search T1 to find if the root of T2 exists within it
-Then we could search just that subtree to see if T2 matches with that subtree
-Things to consider: if there is more than 1 instance of T2.root then that will add to the time complexity. Also null nodes will not show up in an array if not accounted for 
which may hide differences between subtrees
-If you take T1 and turn it into a substring and take substring T2 and compare it it may be faster but much larger in terms of memory capacity
-In order to accomplish the first approach we much have a function that searches through a tree for a specific node.
-Whenever that node is found it runs another function that searches through that subtree comparing it to T2
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f'{self.data}'


def check_subtree(tree1, tree2):
    """Checks tree1 for tree2.root, if tree2.root is found then compare subtrees"""
    print(tree1, tree2)
    if not tree1 and not tree2:
        return True
    elif not tree1 or not tree2:
        return False
    elif tree1.data == tree2.data and compare_subtrees(tree1, tree2):
        return True
    else:
        return check_subtree(tree1.left, tree2) or check_subtree(tree1.right, tree2)


def compare_subtrees(haystack_node, needle_node):
    """Compares haystack node to needle node.root."""
    print('Comparing subtrees')
    print(haystack_node, needle_node)
    # If both nodes are none then we are at the end of each tree
    if haystack_node is None and needle_node is None:
        return True
    elif haystack_node is None or needle_node is None:
        return False
    elif haystack_node.data != needle_node.data:
        return False
    # If both nodes.data match then recurse for left and right nodes
    else:
        return compare_subtrees(haystack_node.left, needle_node.left) and compare_subtrees(haystack_node.right, needle_node.right)


# Testing:

tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(3)
tree1.left.left = Node(4)
tree1.right.right = Node(5)

tree2 = Node(2)
tree2.left = Node(4)

if __name__ == "__main__":
    print(check_subtree(tree1, tree2))

