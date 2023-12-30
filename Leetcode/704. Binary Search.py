"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

Approach:
-Brute force:
-Look at the middle value, if it's not the target then look to the left or right depending on if target is > or <
the middle value
"""

def binary_search_recursive(start, end, nums, target):
    # Base case: If target does not exist then return -1
    if start > end:
        return -1
    
    # Find middle index
    middle = (start + end)//2

    # If middle value is == target then return target
    # If not then search left array or right array depending on target vs index value
    if nums[middle] == target:
        return middle
    elif nums[middle] > target:
        return binary_search_recursive(start, middle-1, nums, target)
    elif nums[middle] < target:
        return binary_search_recursive(middle+1, end, nums, target)
    
def binary_search_iter(nums, target):
    start = 0
    end = len(nums)-1

    while start < end:
        mid = (start + end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid-1
        elif nums[mid] < target:
            start = mid+1
    return -1
        
    
# Testing:
if __name__ == "__main__":
    # nums = [-1,0,3,5,9,12]
    # target = 9
    nums = [-1,0,3,5,9,12]
    target = 2
    print(binary_search_recursive(0, len(nums)-1, nums, target))
    print(binary_search_iter(nums, target))