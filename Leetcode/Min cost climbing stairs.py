""""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


Brute force:
-Traverse the list and compare 2 indices at a time
-choose the lowest one and then compare the next 2 indicies
"""

# Brute force:

def min_cost(cost, price):
    print(cost, price)
    if len(cost) == 1:
        return 0
    
    elif len(cost) > 1:
        second = cost.pop()
        first = cost.pop()
        if second < first:
            price += second
            cost.append(first)
            return min_cost(cost, price)
        price += first
        return min_cost(cost, price)
    return price


# Testing:

if __name__ == "__main__":
    price = 0
    cost = [1,100,1,1,1,100,1,1,100, 1]
    # cost = [1]
    print(min_cost(cost, price))