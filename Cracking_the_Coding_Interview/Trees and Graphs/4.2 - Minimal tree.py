""" 
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create 
a binary search tree with minimal height.

ex. 
array = [1,3,5,6,7,8,12,15,27,38,49,50,65,67,99]

array = [1,3,5]

Tree = 
          15
     6           50
 3     8     38     67
1 3  7 12  27 49  65  99

Node:
-data
-left
-right
Tree:
-add
-remove
-find

Approach:
-Find half way through list, if list has even number then pick the number on the right
-Take that number and set as root
-Find and take middle of left and right halves and set them as left and right node for root respectively
-Repeat this until all elements in array are in the tree
-Steps may differ if len(array is odd vs even)

"""
# Regression:
# Base case: 

# Find middle index with (len(array)/2)-1, if it's not an integer then round up
# Take index and set value as current node
# For 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def minimalTree(array, start, end):
    if start > end:
        return
    mid_index = (end + start)//2
    new_node = Node(array[mid_index])
    print('new_node:', new_node.data)
    new_node.left = minimalTree(array, start, mid_index-1)
    new_node.right = minimalTree(array, mid_index+1, end)
    return new_node
    

if __name__ == "__main__":
    test_array = [1,2,3,4,5,6,7,8,9]
    print(minimalTree(test_array, 0, len(test_array) - 1))