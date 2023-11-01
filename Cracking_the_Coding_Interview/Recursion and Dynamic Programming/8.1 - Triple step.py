"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.

Input: 5
Output: 13; [[1,1,1,1,1], [1,1,1,2], [1,1,2,1], [1,2,1,1], [2,1,1,1], [1,2,2], [2,1,2], [2,2,1], [1,1,3], [1,3,1], 
[3,1,1], [2,3], [3,2]]

Input: 4
Output: 7; [[1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [1,3], [3,1], [2,2]]

Input: 3
Output: 4; [[1,1,1], [1,2], [2,1], [3]]

Input: 2
Output: 2; [[1,1], [2]]

Input: 1
Output: 1; [[1]]

Input: 0
Output: 1; [[]]

climb(n) = climb(n-1) + climb(n-2) + climb(n-3)
"""
# Top down w/ memoization
# Initate a dictionary to store calculations
# Base cases 0, 1, 2
# Recurse down while caching
memo = {}
memo[0] = 1
memo[1] = 1
memo[2] = 2

def climb_topdown(n):
    if n in memo:
        return memo[n]
    memo[n] = climb_topdown(n-1) + climb_topdown(n-2) + climb_topdown(n-3)
    return memo[n]

def climb_bottomup(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    a, b, c = 1, 1, 2
    for iteration in range(n-2):
        next = a+b+c
        a = b
        b = c
        c = next
    return next

# Testing: 
if __name__ == "__main__":
    print(climb_topdown(6))
    print(climb_bottomup(6))
        
        
