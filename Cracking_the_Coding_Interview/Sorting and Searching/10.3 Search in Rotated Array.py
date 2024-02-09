"""
Ask:
Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.

EXAMPLE
Input:find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
Output: 8 (the index of 5 in the array)



Notes:
-array rotation means each number shifts index in a particular direction and if the element is at the end of the array and would fall off it
goes to the other side
-We can't necessarily gaurentee that all the elements to the left are smaller and all the ones on the right are bigger
-In a non-rotated array we could do a simple binary search
-A regular binary search would take the middle number and depending of if target > or < mid, search through array[:mid] or array[mid:]
-Because we know that the array was sorted in increasing order to begin with if for [start:end] start > end then this range indicates that it has
the tail wrapping around to the head
-If the target is within that range then we can continue to search, if not then search the other range
-Ex. if 4 is the "mid index" then in a normal binary search it would look to the left because 25>5 and for our purposes that does not work
-So for our problem we need to look at index 0 to determine where we need to look after we look at the mid index
-If the left most index == middle then we need to look at the right most index and see if that is different. If so then we search in the right half because all the numbers
in the left half are going to be the same
"""

def search_array(array, start, end, n):
    # Find mid index and compare to target
    # if mid == target then return
    # If there is not a match then compare mid to [0]
    # If [0] < mid then left half is ordered correctly 
    #   If mid is > target search left if not search right
    # If [0] > mid then the right side is ordered correctly
    #   If mid is < target search right if not search left
    # If [0] == mid then search right side

    mid = (end + start)//2
    
    if array[mid] == n:
        return mid
    
    if end < start:
        return None
    
    result = None
    if array[start] < array[mid]:
        if array[mid] > n and n >= array[start]:
            result = search_array(array, start, mid-1, n)
        else:
            result = search_array(array, mid+1, end, n)
    
    elif array[start] > array[mid]:
        if array[mid] < n and n <= array[end]:
            result = search_array(array, mid+1, end, n)
        else:
            result = search_array(array, start, mid-1, n)
    
    else:
        if array[mid] != array[end]:
            return search_array(array, mid+1, end, n)
        else:
            result = search_array(array, start, mid-1, n)
            if result == None:
                result = search_array(array, mid+1, end, n)
    return result

# Testing:
if __name__ == "__main__":
    array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    n = 5
    print(search_array(array, 0, len(array)-1, n))

