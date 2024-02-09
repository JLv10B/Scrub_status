"""
You are a professional robber planning to rob houses along a street. Each house has a certain 
amount of money stashed. All houses at this place are arranged in a circle. That means the first 
house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount 
of money you can rob tonight without alerting the police.
"""
def house_robber(array):
    """
    -Given an array find the maximum sum exculding adjacent digits, the first and last digits count as
    adjacent
    -Because the first and last houses are neigbors if there are 3 houses then return max(array)
    -Calculate the max able to be robbed from [1:] and [:-1] and return the larger number

    input: array = [3,4,5,6,7]
                   [3,4,8,10,7]
    output: int
    """
    #Base case:
    if len(array) == 0:
        return 0
    elif len(array) <= 3:
        return max(array)
    
    # Return max value of [1:] and [:-1]
    return max(max_sum(array[1:], 0), max_sum(array[:-1], 0))

def max_sum(array, i):
    # Base case:
    if i > len(array)-1:    
        return 0
    
    return max(array[i] + max_sum(array, i+2), max_sum(array, i+1))

def house_robber_iter(array):
    """
    Using dynamic programing
    """
    if len(array) == 0:
        return 0
    elif len(array) <= 3:
        return max(array)
    
    # Return max value of [1:] and [:-1]
    return max(max_sum_iter(array[1:]), max_sum_iter(array[:-1]))

def max_sum_iter(array):
    """
    -This function finds the largest amount able to be robbed at the point of reaching this house
    -return a result = max(array[i] + max_sum_iter[i-2], max_sum_iter[i-1])
    """
    max1, max2 = 0, 0
    for i in array:
        result = max(max1 + array[i], max2)
        max1 = max2
        max2 = result
    return result


# testing

if __name__ == "__main__":
    array = [1,2,3,1]
    print(house_robber(array))