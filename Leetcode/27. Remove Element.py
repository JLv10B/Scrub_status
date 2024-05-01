"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

Req:
-Remove occurrences of val in place
-First k elements of nums contain elements that are not equal to val
    -Any occurrences of val that are not at the end of the list need to be replaced
-Return k

Approach:
-Initiate k = 0 to count how many non-val elements are in nums
-Iterate through nums and if element is != val then increment k
    If element is == val then k holds it's place until a non-val element is found and can replace it
"""

def remove_element(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

def remove_element_easy(nums, val):
    while val in nums:
        nums.remove(val)

    return len(nums)

# Testing:
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(remove_element(nums, val))

