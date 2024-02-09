"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner 
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The 
robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include 
any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Break down the problem:
1. Focus on the requirements. Figure out the BigO time/space requirements.

Requirements:

2. What cases do we actually need to handle? Check for edge cases. Come up with example data 
inputs to work through

Edge cases:


3. What does data structure look like to satisfy all the above?

4. Now we can code
"""
def count_unique_paths_II(obstacleGrid):
    if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
        return 0
    
    row,col = len(obstacleGrid), len(obstacleGrid[0])

    previous_row = [0] * col 
    current_row = [0] * col
    previous_row[0] = 1

    for i in range(row):
        if obstacleGrid[i][0] == 1:
            current_row[0] = 0
        else:
            current_row[0] = previous_row[0]
        for j in range(1,col):
            if obstacleGrid[i][j] == 1:
                current_row[j] = 0
            else:
                current_row[j] = current_row[j-1] + previous_row[j]
        previous_row[:] = current_row

    return previous_row[col-1]