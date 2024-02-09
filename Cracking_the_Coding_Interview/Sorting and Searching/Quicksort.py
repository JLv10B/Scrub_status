"""
Quicksort Algorithm:
    -Divide and conquer
        -dividing the input list is referred to partitioning the list
        -Quicksort first selects a pivot element and partitions the list around the pivot
        -putting smaller elements into a low array and larger into high array
        -doing so puts the pivot in the correct position
        -can now recursively apply the same procedure to low and high until entire list is sorted

"""
def quicksort(array):
    if len(array) < 2:
        return array
    
    pivot = array[-1] # Can also use a random index here for more consistent time complexity

    low, same, high = [],[],[]

    for element in array:
        if element < pivot:
            low.append(element)
        elif element == pivot:
            same.append(element)
        elif element > pivot:
            high.append(element)

    return quicksort(low) + same + quicksort(high)

# Testing:

if __name__ == "__main__":
    array = [22,11,88,66,55,77,33,44]
    print(quicksort(array))