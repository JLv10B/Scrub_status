"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

ex
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Req:
- Return amount of water that the elevation map can trap
- Find all 'valleys' that can hold water, calculate how much water can be held and sum to find the total
- Valley is defined as having 2 peaks with a low point in between
- A peak is a point that is adjacent to points that are lower
- To determine the amount of water that can be held in a valley you take the smaller of the 2 peaks and subtract each elevation point from that height to find the amount of water
able to be stored at each point
"""