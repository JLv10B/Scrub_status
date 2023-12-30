"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Input array:
[
    1,
    2,
    3,
    4,
    ...
]

Output: False

Time, Space: O(n), O(n)
"""
def contains_dups(array):
    """
    -Iterate through the array and store each element in a set()
    -If an element is already in the set() then return True
    Input: [1,2,3,4,4]
    Output: True, (1,2,3,4)
    """
    # Initiate nums = set()
    # Iterate through array and check if element in nums, if not then add, if yes then return true
    nums = set()
    for element in array:
        if element not in nums:
            nums.add(element)
        else:
            return True
    return False
