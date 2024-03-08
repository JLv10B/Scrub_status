"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be 
numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

ex.
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

req:
- Only uses constant extra space
- return an array with index of the numbers that add to target where 1 <= index1 < index2 <= numbers.length.

Aproach:
- Because numbers is given in non-decending order we know the smallest numbers are on the left and the largest
numbers are on the right. We can add the 2 ends and depending on the sum adjust the right or left pointer to 
give us a smaller or larger number until target is found.
- Initialize left, right = 0, len(numbers)-1
- Add numbers[left] and numbers[right], if the sum is > target then decrement right, if sum is < target
increment left, if sum is == target return (left+1, right+1)

Space: O(1)
"""

def two_sum_constant_space(numbers, target):
    left, right = 0, len(numbers)-1

    while left < right:
        if (numbers[left] + numbers[right]) > target:
            right -= 1
        elif (numbers[left] + numbers[right]) < target:
            left += 1
        else:
            return (left+1, right+1)
        
# Testing:
        
if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(two_sum_constant_space(numbers, target))