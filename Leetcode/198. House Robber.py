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
    Input:
    array = [
                10,
                500,
                100,
                50,
                ...
            ]

    Output:
    sums = [
            10,
            500,
            110,
            550,
            ...    
            ]
    max_money = 550
    

    """
    memo = {}
    def helper(i):
        if i >= len(array):
            return 0
        res = max(array[i] + helper(i+2), helper(i+1))
        if i not in memo:
            memo[i] = res
        return res
    return helper(0)

# Testing:
if __name__ == "__main__":
    array = [10,500,100,50]
    print(house_robber(array))