"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

ex.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-20,7,8]
Output: 23
"""
from math import inf

def largest_subarray_sum(nums):
    """
    This function takes a list as input and returns the largest sum of a subarray.

    Approach:
    - In the given array nums we can have neg int, pos int, and 0. In order to justify a neg int n then the array to the right of n must be greater than abs(n).
        - eg. if nums[3] = -10 then nums[4:] must be >10 in order to justify including nums[3] in the subarray
    - Initialize largest_sum, current_sum = float('-inf'), 0
    - Iterate through nums, add each val to current_sum and set largest_sum = max(largest_sum, current_sum)
    - If current_sum < 0 then reset current_sum to 0
        - If current_sum is negative then the largest sum of the current subarray has been calculated and the current_sum should be reset to calculate the next subarray

    """

    largest_sum, current_sum = float('-inf'), 0

    for val in nums:
        current_sum += val
        largest_sum = max(current_sum, largest_sum)
        if current_sum < 0: # Start calculating the sum of a new subarray
            current_sum = 0

            
    return largest_sum

# Testing:
if __name__ == "__main__":
    nums = [5,4,-1,7,8]
    print(largest_subarray_sum(nums))
        
