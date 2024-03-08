"""
Given an array of integers nums and an integer target, return indices of the two numbers such 
that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input array:
nums = [1,3,7,10]
target = 8

Output array = [0,2]

Req:
- Determine whether there are 2 elements that sum to target
- Return indicies of the 2 numbers that sum to target
- Cannot reuse elements

Approach:
- To find if there are 2 elements that sum to target we can iterate through the input array and subtract that 
element from the target to find the remainder. If the remainder has already been seen then we can return
the indicies. If the remainder has not been seen then store the element and index in a dictionary.
- Create a dictionary with element:index which holds each element

"""
def two_sum(nums, target):
    # Initialize remainder_dict {}
    remainder_dict = {}

    # For each element in nums array find remainder
    # If remainder is in remainder_dict then return indicies
    # If remainder is not in remainder_dict then store element:index
    for i in range(len(nums)-1):
        remainder = target - nums[i]
        if remainder in remainder_dict:
            return i, remainder_dict[remainder]
        else:
            remainder_dict[nums[i]] = i

    return False
        
# Testing:
if __name__ == "__main__":
    nums = [5,1,5,11]
    target = 10
    two_sum(nums, target)

