"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

reqs:
-return max water

- start at the 2 end points to calculate max water
- move the smaller wall towards the other wall
- if the walls overlap or cross then return max water

time:O(n)
space:O(n)

"""
def find_max_water(height):
    max_water = 0

    left = 0
    right = len(height)-1

    while left < right:
        current_water = min(height[left], height[right]) * abs(right-left)
        max_water = max(current_water, max_water)

        if height[left] < height[right]:
            left += 1
        else:
            right -=1

    return max_water
