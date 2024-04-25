"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Req:
-How many plots can we plant?
    - Need counter to track how many plots can be planted, must == n
-Can we plant a flower at this plot?
    -A plot can be planted if it is not adjacent to a 1
-Increment counter when a plot is determined to meet criteria

Approach:
-Initiate counter to track number of plots that meet criteria
-If the current element is 0
    -If the next plot is also 0 or current element is at the end of the flowerbed then we can increment the counter
        -Move current element 2 spaces
    -If the next plot is 1 then increment current element by 1
-If the current element is 1 then we don't increment the counter and we skip the next plot
-If counter >= n then return True, else false
"""

def can_place_flowers(flowerbed, n):
    plots_meeting_criteria = 0
    current_element = 0
    next_element = 0

    if n == 0:
        return True

    while current_element <= len(flowerbed)-1:
        if flowerbed[current_element] == 1:
            current_element += 2
        else:
            next_element = current_element+1
            if (next_element > len(flowerbed)-1) or (flowerbed[next_element] == 0):
                plots_meeting_criteria += 1
                current_element += 2
            else:
                current_element += 1
            if plots_meeting_criteria >= n:
                return True
            
    return False

# Testing:
if __name__ == "__main__":
    flowerbed = [1]
    n = 0
    print(can_place_flowers(flowerbed, n))
