"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

ex
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Req:
- Return amount of water that the elevation map can trap
- At any given location on the elevation map the water that can be held at that location [i] is determined by min(max_left, max_right) - height[i] 
if this results in a negative number then there cannot be any water held at [i]
- To find the max_left and max_right at [i] we can iterate through the array from left to right recordding the largest number then perform the same from right to left
- Then we can iterate through each index and calculate how much water can be contained and return the result

Datastructure:
-2 arrays to hold max_left & max_right that are the same lenght as the input array
"""

def trap_rain_water(height):
    # Intilize max_left & max_right & trapped_water
    max_left = [0] * len(height)
    max_right = [0] * len(height)
    result = 0

    # Iterate through height and record max value at each index in max_left then perform the same in reverse, start at 1 and 2nd to last index because ends will always be 0
    for i in range(1, len(height)):
        max_left[i] = max(height[i-1], max_left[i-1])
        
    for i in range(len(height)-2, -1, -1):
        max_right[i] = max(height[i+1], max_right[i+1])

    print(f'max left = {max_left}')
    print(f'max right = {max_right}')

    for i in range(len(height)):
        trapped_water = min(max_left[i], max_right[i]) - height[i]
        if trapped_water > 0:
            result += trapped_water

    return result

def trap_rain_water_efficient(height):
    left = 0
    right = len(height)-1
    max_left = height[left]
    max_right = height[right]
    result = 0

    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, height[left])
            result += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            result += max_right - height[right]

        print(f'max_left = {max_left}, max_right = {max_right}')

    return result


# Testing:
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap_rain_water(height))
    print(trap_rain_water_efficient(height))