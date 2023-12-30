"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,4,3,1]
Output: 0

Approach:
-Brute force:
-Starting at the beginning, compare first 2 index
-If the later index is smaller than the first index then replace first index and move 2nd index
-If 2nd index is larger than first index then save the profit in max_profit and move the 
2nd index over until end of array or another larger value is found
-If the 2nd index finds a value less than the first index then move the first index there and cotinue
"""

def best_profit(prices):
    # Initiate l => points at index, max_price = 0
    l = 0
    max_profit = 0
    buy = 0
    sell = 0

    # Right pointer iterates through the array
    # If prices[l] is < prices[r] then calculate max_price
    # If prices[l] > prices[r], move l to r
    for r in range(len(prices)):
        if prices[l] > prices[r]:
                l = r
        if l < r:
            profit = prices[r] - prices[l]
            if max_profit < profit:
                max_profit = profit
                buy = l
                sell = r

    return print(f'Max profit: {max_profit}, Buy date: {buy}, Sell date: {sell}')
            

# Testing:
if __name__ == "__main__":
    prices = [7,2,5,3,6,4,1,10]
    # prices = [7,6,4,3,1]
    best_profit(prices)