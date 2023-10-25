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
-If the T1 subtree does not match with T2 then continue to search T1 but skip the nodes that have been processed already
-Another thing to consider is whether it's better to preprocess T2 vs process it at the same time as the subtree in T1
-


"""
class Node:

class BinaryTree:

def check_subtree(tree1, tree2):
    """ Searches tree1 for tree2.root, searches should be done by BFS """
    # If tree2.root is found, run compare function


def process_tree(tree2):
    """ Processes tree to create an array """


def compare_subtrees(node, visited):
    """Compare subtree (starting at node as root) to processed tree2. Output should include visited in order to not search through the same nodes again if subtrees do not match
    Input: node, [visited]
    Output: Boolean, [visited]
    """


