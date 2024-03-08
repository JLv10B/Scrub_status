"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result 
must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Req:
- Return any overlapping elements without repeats

Approach:
- Initialize result = [], seen = set()
- Iterate through the smaller array
    - Add element to seen
    - If element is in the other array append to result
- Return result
"""

def intersection(nums1, nums2):
    if len(nums1) > len(nums2):
        long = nums1
        short = nums2
    else:
        long = nums2
        short = nums1

    result = []
    seen = set()

    for i in short:
        if i in seen:
            continue
        else:
            seen.add(i)
            if i in long:
                result.append(i)
    
    return result

def intersection_optimal(nums1, nums2):
    result = list(set(nums1).intersection(set(nums2)))
    return result
# Testing:
if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(intersection(nums1, nums2))
    print(intersection_optimal(nums1, nums2))
