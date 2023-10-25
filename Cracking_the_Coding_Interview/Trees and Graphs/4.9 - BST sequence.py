"""
A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.

Ex.
Input: 
                    50 
        20                    60
    10                  55
Output: [50,20,60,10,55], [50,60,20,10,55], [50,20,60,55,10], [50,60,20,55,10]

Approach:
-In order to create a binary serach tree we must input the left and right subtrees/nodes in the appropriate order.
-Each depth per subtree must maintain relative order but left vs. right does not matter

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while current_node:
            if current_node.data > data:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                else:
                    current_node = current_node.left
            if current_node.data < data:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right

# Function finds all sequences that can be input to create BST
def find_bst_sequences(tree):
    # If tree is empty return empty array
    # If non-empty tree, utilize helper function
    if tree.root is None:
        return []
    else:
        return helper(tree.root)
    

def helper(node):
    """ This function utilizes the weave function to create sequences starting at the input node """
    # If input is an empty node, such as a leaf, return [[]]
    if node is None:
        return [[]]
    
    # right_subtree goes down the path of the right node
    # left_subtree goes downt he path of the left node
    right_subtree = helper(node.right)
    left_subtree = helper(node.left)
    sequences = []

    # For each different ordering in the right_subtree and left_subtree
    # Weave together each ordering/sequence behind the input/parent node
    for right_sequence in right_subtree:
        for left_sequence in left_subtree:
            sequences = weave(left_sequence, right_sequence, [node.data], sequences)
    return sequences

def weave(left_sequence, right_sequence, prefix, sequences):
    """This function takes the left and right sequences and weave it together beind the prefix and save it in sequences"""
    # If left_sequence or right_sequence is empty then add the non-empty sequence to the prefix
    if len(left_sequence) == 0 or len(right_sequence) == 0:
        result = prefix.copy() # This must be a .copy() in order to not modify the prefix for later
        result.extend(left_sequence)
        result.extend(right_sequence)
        sequences.append(result)
        return sequences
    
    prefix.append(left_sequence[0])
    sequences = weave(left_sequence[1:], right_sequence, prefix, sequences)
    prefix.pop()
    prefix.append(right_sequence[0])
    sequences = weave(left_sequence, right_sequence[1:], prefix, sequences)
    prefix.pop()
    return sequences

# Testing:

def example():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    # bst.insert(11);
    # bst.insert(14);

    sequences = find_bst_sequences(bst)
    print(sequences)

if __name__ == "__main__":
    example()