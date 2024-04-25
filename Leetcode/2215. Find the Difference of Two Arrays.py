"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

example:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]

Req:
-Return 2 nested lists that contain the numbers that aren't shared in nums1 and nums2 respectively
    -Brute force: 
        -create a set for each list to store all unique numbers for repective list
        -Iterate through each list to find the numbers that do no overlap and place it in the repective answer list
        -O(n^2)
    -Set subraction:
        -convert lists into sets
        -subtract sets from each other to find the non shared numbers for each respective list
            -convert answer into list
        -return both lists nested in a list
        
"""

def difference_between_two_arrays(nums1, nums2):
    unique_nums1 = set(nums1)
    unique_nums2 = set(nums2)
    answer1 = list(unique_nums1 - unique_nums2)
    answer2 = list(unique_nums2 - unique_nums1)

    return [answer1, answer2]

# Testing:
if __name__ == "__main__":
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    print(difference_between_two_arrays(nums1, nums2))