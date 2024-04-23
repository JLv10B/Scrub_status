"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

examples:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

Input: arr = [400]
Output: [-1]

Req:
-Replace each element with the greatest element to the right
-Replace last element with -1

Approach:
-Can be performed in place, do not need an additional data structure
-Starting from the right most element, store the element and replace it with -1
    -Stored element is the current largest element to the right
-Traverse left store the current element in another variable and replace it with the current largest element to the right
    -Compare current element to the largest element to the right, replace if current element is larger

"""
def replace_with_greatest_right_element(array):
    current_element = 0
    largest_right_element = array[-1] # Stores last element because it will get replaced

    for index in range(len(array)-1,-1,-1):
        if index == len(array)-1:
            array[index] = -1
        else:
            current_element = array[index]
            array[index] = largest_right_element
            largest_right_element = max(current_element, largest_right_element)

    return array
    
# Testing
if __name__ == "__main__":
    array = [17,18,5,4,6,1]
    print(replace_with_greatest_right_element(array))
