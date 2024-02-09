"""
You are given an integer array height of length n. There are n vertical lines drawn such that the 
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Break down the problem:
1. Focus on the requirements. Figure out the BigO time/space requirements.

Requirements:
-Find the maximum amount of water that can be stored given array
-To find the maximum amount of water we take the smaller of the 2 walls and multiply it by the distance btwn
-We have 3 variables, left wall, right wall, and distance
-The longest distance is the length of the array so [0] and [-1] will be the furthest distance
-So we want to find the tallest walls that are the furthest apart
-This likley can be done in O(n) time with O(1) space

2. What cases do we actually need to handle? Check for edge cases. Come up with example data 
inputs to work through

Edge cases:
None?
Input: [0,5,7,3,4,6,7,8]
Output: 35

3. What does data structure look like to satisfy all the above?

array

4. Now we can code

"""
def most_water(array):
    # Initiate 2 pointers left = 0 and right = len(array)-1
    # Initiate max_water = 0 to hold max water calculated
    left = 0
    right = len(array)-1
    max_water = 0
    
    # While left and right pointers have not crossed we continue to check if we can hold more water
    # Increment the smaller wall inwards and recacluate until basecase is reached
    while left <= right:
        contained_water = min(array[left], array[right]) * abs(left-right)
        max_water = max(max_water, contained_water)

        if array[left] <= array[right]:
            left += 1

        else:
            right -= 1
    
    return max_water

if __name__ == "__main__":
    array = [0,5,7,3,4,6,7,8]
    print(most_water(array))