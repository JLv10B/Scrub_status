"""
Given an array of integers nums and an integer target, return indices of the two numbers such 
that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input array:
nums = [
        1,
        3,
        7,
        10,
        ...
        ]
target = 8

Output array = [0,2]

O(n), O(n)
"""
def two_sum(nums, target):
    """
    -Subtract each number in nums from target to get remainders
    -If remainder is in the given array then return indecies

    Input array:
    nums = [5,1,5,11]
    target = 10

    Output = 0,2
    """
    # Initiate {remainders}
    remainders = {}

    # Iterate through enumerate(nums)
    # Subtract each number from target to get remainder
    # Check if remainder is in remainders
    # If not then remainders[number] = index
    # If remainder found in remainders then return index of current number and index of remainder
    for index, number in enumerate(nums):
        rem = target - number
        if rem not in remainders:
            remainders[number] = index
        else:
            return(print(index, remainders[rem]))
        
# Testing:
if __name__ == "__main__":
    nums = [5,1,5,11]
    target = 10
    two_sum(nums, target)

