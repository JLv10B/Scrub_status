"""
A magic index in an array A [ 0••• n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?

Notes:
-Iterate through the array
-If index == A[index]
-Store in [magic_index]
"""
def magic_index_iterative(array):
    for index in range(len(array)):
        if array[index] == index:
            return print(index)
    return print('No magic index')


def magic_index_recursive(array, start, end):
    if end < start:
        return print('No magic index')
    mid = (start + end)//2
    if mid == array[mid]:
        return print(array[mid])
    elif mid > array[mid]:
        return magic_index_recursive(array, mid+1, end)
    else:
        return magic_index_recursive(array, start, mid-1)

# Testing:
if __name__ == "__main__":
    a = [-40,-10,0,1,4,8,9,15,27,48,59,50]
    magic_index_recursive(a, 0, len(a)-1)
    magic_index_iterative(a)

