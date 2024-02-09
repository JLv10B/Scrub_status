"""
You are given an integer array nums. You are initially positioned at the array's first index, and each 
element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

ex.
Input: nums = [2,3,1,1,4]
Output: true

Input: nums = [3,2,1,0,4]
Output: false

Break down the problem:
1. Focus on the requirements. Figure out the BigO time/space requirements.

Requirements:
-Given an array of max jump values can we reach the last index of the array
-Go backwards staring from nums[-2] and find if it's possible to get to the last index, if yes return True
if no return False

-Time: O(n)
-Space: O(n)

2. What cases do we actually need to handle? Check for edge cases. Come up with example data 
inputs to work through

3. What does data structure look like to satisfy all the above?

array

4. Now we can code
"""
def jump_game(nums):
    goal = len(nums)-1

    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    
    return True if goal == 0 else False

# Testing:
if __name__ == "__main__":
    nums = [3,2,2,0,4]
    print(jump_game(nums))
