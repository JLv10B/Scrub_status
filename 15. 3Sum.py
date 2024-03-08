"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Req:
- return an array of triplets that sum to 0
- Can't repeat indecies in a triplet

Approach:
- Initialize result = set()
- sort nums with sort()
- Iterate through indecies of nums[:-2], initialize mid = i+1, right = len(nums)-1
- To avoid duplicate triplets as we iterate through nums if nums[i] == nums[i-1] then continue
- while right > mid
- If the sum of the 3 values is < 0 then increment mid
- If sum is > 0 then decrement right 
- If sum is == 0 add to result, increment mid and decrement right because if mid changes then right has to change
- To avoid duplicate triplets if nums[mid] is the same as the previous then continue to increment, if nums[right] is
the same as the previous then continue to decrement
- return result
"""

def three_sum(nums):
    result = set()
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        mid = i+1
        right = len(nums)-1
        while right > mid:
            val_sum = nums[i] + nums[mid] + nums[right]
            if val_sum < 0:
                mid += 1
            elif val_sum > 0:
                right -= 1
            else:
                result.add((nums[i], nums[mid], nums[right]))
                mid += 1
                right -= 1
                while right > mid and nums[mid] == nums[mid-1]:
                    mid += 1
                while right> mid and nums[right] == nums[right+1]:
                    right -= 1
                
    return result

"""
Alternative approach:
- results = set()
- Sort nums into 2 dictionarys non-zero pos int and non-zero neg int, while sorting count how many 0s there are
- If there is a 0 then iterate through the pos_int dict and check if there is the negative in neg_int
- If there are 3 0s then add [0,0,0] to results
- Take pairs from the pos_int and neg_int lists and calculate what number is needed to sum to 0, if that number
is in the other list then add it to results
"""
from collections import defaultdict

def three_sum_dict(nums):
    result = set()
    pos_int = []
    neg_int = []
    zeros = 0

    for n in nums:
        if n > 0:
            pos_int.append(n)
        elif n < 0:
            neg_int.append(n)
        else:
            zeros += 1

    if zeros:
        for val in pos_int:
            if -val in neg_int:
                result.add(tuple(sorted((val, 0-val, 0))))
        if zeros > 2:
            result.add((0,0,0))

    nums_set = set(nums)
    for num_list in [neg_int, pos_int]:
        for i in range(len(num_list)):
            for j in range(i+1, len(num_list)):
                target = -(num_list[i]+num_list[j])
                if target in nums_set:
                    result.add(tuple(sorted((num_list[i],num_list[j],target))))

    return result

# Testing:
if __name__ == "__main__":
    nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
    # print(three_sum(nums))
    print(three_sum_dict(nums))
    
        
            