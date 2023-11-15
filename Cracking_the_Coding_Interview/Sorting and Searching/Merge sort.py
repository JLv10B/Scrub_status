"""
Merge sort algorithm:
    -Divide and conquer algorithm
        -Breaks down problems into multiple subproblems until they become simple to solve
        -Solutions are combined to solve original problem
    -O(nlogn) run time
    -General principle
        -Split array in half
        -Call merge sort on each half to sort them recursively
        -Merge both sorted halves into one sorted array
            -This does the heavy lifting
"""

def merge_sort(array):
    if len(array) == 1:
        return array
    
    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        # Recursion
        merge_sort(left_array)
        merge_sort(right_array)

        # Merge
        left = 0 # left array index
        right = 0 # right array index
        merged = 0 # merged array index

        while left < len(left_array) and right < len(right_array):
            if left_array[left] < right_array[right]:
                array[merged] = left_array[left]
                left += 1
            else:
                array[merged] = right_array[right]
                right += 1
            merged += 1

        while left < len(left_array):
            array[merged] = left_array[left]
            left += 1
            merged += 1

        while right < len(right_array):
            array[merged] = right_array[right]
            right += 1
            merged += 1

    return array

# Testing:

if __name__ == "__main__":
    array = [1,4,6,8,0,13,25,47,39,15,12,14,4,5,7]
    print(merge_sort(array))