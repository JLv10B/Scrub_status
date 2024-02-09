"""
You are a professional robber planning to rob houses along a street. Each house has a certain 
amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent 
houses have security systems connected and it will automatically contact the police if two adjacent 
houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount 
of money you can rob tonight without alerting the police.

Notes:
-Can't rob adjacent homes

Input:
[
    10,
    500,
    100,
    50
]

Output: 550, max amount of money you can rob
"""
def house_robber(array):
    """
    -Given array of numbers we can use recursion to find the max sum at each index within the given
    restrictions

    [1,2,3,4,5]
    """
    # If length of array is <=2 then return the max, covers 0,1,2
    if len(array) == 0:
        return 0
    elif len(array) <= 2:
        return max(array)
    
    # Find the max sum
    return max_sum(array, 0)

def max_sum(array, i):
    # Base case: if index is > len(array)-1 then all houses are accounted for
    if i > len(array)-1:
        return 0
    
    # Recursive case: which is greater, the current house + the max_sum at the skip house or the max_sum
    # at the next house
    return max(array[i]+max_sum(array, i+2), max_sum(array, i+1))
    

# Testing:
if __name__ == "__main__":
    array = [10,500,100,50,10,15,80]
    # array = []
    print(house_robber(array))