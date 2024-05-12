"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

example:
Input: prices = [7,1,5,3,6,4]
Output: 7

Input: prices = [1,2,3,4,5]
Output: 4

Req:
-Return the maximum profit we can achieve
    -buy low, sell high
    -calculate profit between subsiquent days and sum if > 0

Approach:
-Initiate profit= 0
-Iterate through prices, if prices[i+1] - prices[i] then add to profit
return profit
"""
def best_time_to_buy_sell(prices):
    profit = 0

    for i in range(len(prices)-1):
        if prices[i+1] - prices[i] > 0:
            profit += (prices[i+1] - prices[i])

    return profit

# Testing:
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    # prices = [1,5,4,7,4,9,10,11,1]
    print(best_time_to_buy_sell(prices))
