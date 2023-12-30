"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Notes:
-brute force: for each index we can take that element out of the list and multiply the rest

-more efficient:
-Initiate an array of [1] * len(array)
-For each index of the array calculate the the product of all the indicies before and after using [answer]
to store values


"""

def product_bruteforce(array):
    answer = []
    for index in range(len(array)):
        x = 1
        new_array = array.copy()
        new_array.pop(index)
        for n in new_array:
            x = x*n
        answer.append(x)
    return answer

def product_efficient(array):
    # Initiate answer array
    answer = [1] * len(array)

    # pre = holds product of values prior to array[i], initate as 1
    pre = 1
    # Iterate through the array
    for i in range(len(array)):
        answer[i] = pre
        pre *= array[i]
    # post = hold product of values after array[i], initate as 1
    post = 1
    # Iterate through the array in reverse
    for i in range(len(array)-1, -1, -1):
        answer[i] *= post
        post *= array[i]
    return answer


# Testing:

if __name__ == "__main__":
    array = [1,2,3,4]
    # array = [-1,1,0,-3,3]
    print(product_bruteforce(array))
    print(product_efficient(array))

    