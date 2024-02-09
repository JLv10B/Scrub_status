"""
You are given an integer array coins representing coins of different denominations and an integer amount 
representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by 
any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

Requirements:
Input: coins = [1,2,5], amount = 5
- Return the number of combinations that make up amount

Cases:
- We can consider using [], [1], [1,2], [1,2,5] and build dynamic programming arrays
- Each DP array holds how many ways we can create the amount with the coins provided
- We start by considering no coins, then only one coin then we continue to add on with additional coins

        0     1     2     3     4     5   <- Amount
[]      1     0     0     0     0     0   <- Base
[1]     1     1     1     1     1     1   <- Current
[2]     1     1     2     2     3     3
[5]     1     1     2     2     3     4

- The base array is initialized the same for any input, Base[amount] is how many ways you can create
amount from no coins

- Constructing current array:
- if amount is >= current coin then subtract current coin to find remainder
- take base[amount] and add to current[remainder] = how many ways to create amount with current coins
- After we create our current dp array we can set Base as current and recreate the current array with a 
new coin

- Return current[-1]

"""
def coin_change_perm_count(amount, coins):
    # Initialize base and current array
    base = [0] * (amount+1)
    current = [0] * (amount+1)
    base[0], current [0] = 1, 1
    
    # Iterate through [coins] to construct current array
    # Solve subproblems for 0 to target amount
    # If sub_amount >= coin then subtract to find remainder
    # base[sub_amount] + current[remainder]
    # Once we've reached target amount then set base = current
    for coin in coins:
        for sub_amount in range(amount+1):
            if sub_amount >= coin:
                remainder = sub_amount - coin
                current[sub_amount] = base[sub_amount] + current[remainder]
            else:
                current[sub_amount] = base[sub_amount]
        base = current

    return current[-1]

# Testing:
if __name__ == "__main__":
    amount = 150
    coins = [1,2,5,10,25]
    print(coin_change_perm_count(amount, coins))
