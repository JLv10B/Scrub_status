"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Example 2:
Input: intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
Output: [[1,10]]
"""

def merge_overlapping_intervals(intervals:list):
    """
    This function accepts a list of intervals written as [start, end] and returns a list of intervals such that any overlapping intervals are marged into a single interval.

    Approach:
    - In order to know whether we should merge 2 intervals we can see if one overlaps with the other, if they do then merge
    - Because intervals can be given in any order, intervals should be sorted by start values to avoid having to recheck every interval that has already been appended to the result array
    - If len(intervals) == 0, return []
    - Sort intervals by start values
    - Initialize result = []
    - If len(result) == 0 or there is no overlap between result[-1] and the current interval then append the current interval to result
    - If there is an overlap then update result[-1] to reflect merged interval
    - Return result
    """
    
    if len(intervals) == 0:
        return []
    
    intervals.sort(key = lambda x: x[0]) # Sort in place vs using sorted which returns a new list
    result = []

    for interval in intervals:
        if (len(result) == 0) or interval[0] > result[-1][1]:
            result.append(interval)
        else:
            result[-1][0] = min(result[-1][0], interval[0])
            result[-1][1] = max(result[-1][1], interval[1])

    return result

# Testing:
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[12,18]]
    print(merge_overlapping_intervals(intervals))