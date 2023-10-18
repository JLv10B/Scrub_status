""" 
Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists). 

Ex.
Binary Tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
    }

A -> root (1st depth)
B, C -> 2nd depth
D, E, F, G -> 3rd depth
...

Children of nodes form the next depth/desired linked list in our case

In order to create linked lists for each depth:
-Start at root which is the first depth
-Traverse the tree with breadth first search algo to hit each child node
-The children of each depth are going to make up all the nodes of the next linked list
-As you traverse each node to add to linked list append the child nodes to queue
-Need to define Node() and TreeNode()
"""

# Tree_node class - data, left, right
class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# LinkedList_node class = data, next
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def list_of_depths(root):
    if root is None:
        return('No nodes')
    
    # Initiate [queue] with root, [results] to store linked lists
    queue = [root]
    results = []
    # While [queue] has values find the length in order to count how many nodes should be in the new linked list
    # Initate linked_list = None and tail = None to hold head and tail
    while queue:
        list_length = len(queue)
        linked_list = None
        tail = None
        
        # For each count in len[queue]
        # Pop the first value
        # Create a new LinkedList_node
        for count in range(list_length):
            tree_node = queue.pop(0)
            new_node = LinkedListNode(tree_node.data)
       
            # If linked_list = None then set the new node as linked_list and tail
            # If linked_list then set new node as tail.next
            if linked_list is None:
                linked_list = new_node
                tail = new_node
            else:
                tail.next = new_node

            if tree_node.left:
                queue.append(tree_node.left)
            if tree_node.right:
                queue.append(tree_node.right)
        # After the loop append linked_list, linked list head, to [results]
        results.append(linked_list)
    
    # Return [results]
    return results

# Testing
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print(list_of_depths(root))
