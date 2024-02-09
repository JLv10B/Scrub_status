"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Input:
nums = [1,4,6,8,9,12,15,19]

Output:
            9
        6        15
    4      8   12   19
1

O(n), O(n)
"""
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def array_BST(nums):
    """
    -Find the middle element of the original array, this is the root node
    -Find the middle element of the left array, this is node.left
    -Repeat for the right array, this is node.right
    -Use a helper function to recurse through the array
    
    """
    
    def helper(start, end):
        # Base case:
        if start > end:
            return
        
        # Find middle element and set that as the node
        mid = (start + end)//2
        node = Node(nums[mid])
        
        # Find the left and right children by recursing through the left and right half of the array
        node.left = helper(start,mid-1)
        node.right = helper(mid+1,end)
        return node
    
    return helper(0, len(nums)-1)
    
