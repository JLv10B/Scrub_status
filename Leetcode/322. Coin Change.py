"""
You are given an integer array coins representing coins of different denominations and an integer 
amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0

"""
import math
def coin_change(coins, amount):
    """
    Input: coins = [4,5,8], amount = 9
    Output: 2
    """
    memo = {}
    def helper(n):
        """
        -This function returns res = the fewest amount of coins that are required to create n
        -n is stored in {memo} as n:res

        example
        Input:
        n = 11
        Output = 3
        """
        # Basecase: target == 0
        if n == 0:
            return 0
        
        # Basecase: check memo for answer
        if n in memo:
            return memo[n]
        
        # Initate res to n+1, if all coins are > n then res will remain n+1 which will return -1
        # Iterate through coins and recurse through each (n-c), incrementing by 1 maintaining count of the
        # subtracted coin
        # Store n in {memo}
        res = n+1
        for c in coins:
            if c<=n:
                res = min(res, helper(n-c)+1)
        if n not in memo:
            memo[n] = res
        return res
    res = helper(amount)
    return res if res <= amount else -1

# Testing:
if __name__ == "__main__":
    # coins = [4,5,8]
    # amount = 9
    coins = [12,12,12]
    amount = 9
    print(coin_change(coins, amount))

    
    


