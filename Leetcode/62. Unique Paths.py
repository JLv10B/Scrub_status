"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either 
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach 
the bottom-right corner.

Break down the problem:
1. Focus on the requirements. Figure out the BigO time/space requirements.

Requirements:
-We are given a graph where we need to find all possible paths from [0][0] to [m-1][n-1]
-The robot cannot move left or up so it cannot back track
-We can do either DFS or BFS, select DFS and add a count to unique paths every time a path reaches [m-1][n-1]
Time: O(n)
Space: O(n)

2. What cases do we actually need to handle? Check for edge cases. Come up with example data 
inputs to work through

Edge cases:
-Robot going out of bounds

Input: m=3 n=2
Output: 3

3. What does data structure look like to satisfy all the above?

4. Now we can code
"""
def count_unique_paths(m,n):
    # Create a dynamic programming array to store count of unique paths to each coord
    # The first row and column should all be 1 because there is only 1 possible path to coords in those row/col
    # The remaining should be initialized to 0
    path_count_matrix = [[1 if row == 0 or col == 0 else 0 for col in range(n)] for row in range(m)]

    for row in path_count_matrix:
        print(row)

    # For each coord starting at [1][1] we add the number to the top and to the left because those are the only
    # possible paths to reach that current coord
    for row in range(1,m):
        for col in range(1,n):
            path_count_matrix[row][col] = path_count_matrix[row-1][col] + path_count_matrix[row][col-1]

    for row in path_count_matrix:
        print(row)

    return path_count_matrix[-1][-1]

#Testing:
if __name__ == "__main__":
    print(count_unique_paths(3,7))