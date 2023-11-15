"""
Ask:
You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.

Input: 
A: [1,5,10,11,15,x,x]
B: [2,6]

Output:
A: [1,2,5,6,10,11,15]

"""
def merge_sort(a, b):
    """ 
    We know that array a is longer than b w/ buffer letters for array b. We can compare the largest elements from each
    array and move it to the back.
    """
    # Pointer for current index
    # Compare largest elements in array a and array b
    # Move the larger element to the end of array a
    # Continue until array b is empty

    pointer = len(a)-len(b)-1
    b_element = len(b)-1
    for index in range(len(a)-1, -1, -1):
        if b_element < 0:
            return a
        if a[pointer] > b[b_element]:
            a[index] = a[pointer]
            a[pointer] = 'x'
            pointer -= 1
        else:
            a[index] = b[b_element]
            b_element -= 1
    return a

# Testing:

if __name__ == "__main__":
    a= [1,5,10,11,15,'x','x']
    b= [2,6]
    
    print(merge_sort(a,b))