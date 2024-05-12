"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

examples:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

Req:
-Sort in place with all 0s to the left, 1s in the middle, and 2s to the right

Approach:
-runner = pointer that iterates left to right
-left = holds a position at the left
-right = holds a position at the right
-If runner is 0 then send it to the left
    -left and runner += 1
-If runner is 2 then send it to the right
    -right -= 1
-If runner is 1 then leave in place
    -left += 1
"""

def sort_colors(nums):
    left, runner, right = 0, 0, len(nums)-1

    while runner <= right:
        if nums[runner] == 0:
            nums[runner], nums[left] = nums[left], nums[runner] 
            runner +=1
            left += 1 # left pointer moves now that we know there is a 0 there
        elif nums[runner] == 2:
            nums[runner], nums[right] = nums[right], nums[runner]
            right -= 1 # right pointer moves now that we know there is a 2 there
        else:
            runner += 1

    return nums

# Testing:
if __name__=="__main__":
    nums = [2,0,2,1,1,0,1,2,0,1,1,1,0]
    print(sort_colors(nums))