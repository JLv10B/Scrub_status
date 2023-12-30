"""
Ask:
Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits"such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.

Given:
-matrix r x c
    -certain cells are off limits/blocked
-robot
    -can only move rigth and down

matrix:
[[0,0,0,0,1,0],
 [1,1,0,1,1,0],
 [0,0,0,0,0,0],
 [0,0,0,0,1,0],
 [1,0,0,0,1,0],
 [0,1,0,0,1,0]
]

start: matrix[0][0]
end: matrix[r-1][c-1]

output:[(0,0), (0,1), (0,2), (1,2), (2,2), (2,3), (2,4), (2,5), (3,5), (4,5), (5,5)]

Approach:
-Start with a container list to store each [path] containing (row, column) as coordinates for the robot
-Initial path starts with only (0,0)
-Iterate through each [path] looking at last coord and checking right and down paths to see if they are open
-If 1 or more is open then append new [path] with new coord to container list
-If both right and down are blocked/untraversable then delete the current path as it's at a dead end

"""

def robot_in_grid(matrix):
    if not matrix:
        return None
    rows = len(matrix)-1
    columns = len(matrix[0])-1
    path_list = []
    failed_points = set()
    if robot_movement(matrix, rows, columns, path_list, failed_points):
        return print(f'Robot path through the matrix: {path_list}')
    return None

def robot_movement(matrix, row, column, path_list, failed_points):
    # Base case is if coordinate is out of bounds or hits a dead end we terminate that path
    if row < 0 or column < 0 or matrix[row][column] == 1:
        return False
    
    coord = (row, column)

    if coord in failed_points:
        return False
    
    if(((row == 0) and (column == 0))
       or robot_movement(matrix, row, column-1, path_list, failed_points) 
       or robot_movement(matrix, row-1, column, path_list, failed_points)):
        path_list.append(coord)
        return True
    
    failed_points.add(coord)
    return False

def robot(matrix):
    rows, columns = len(matrix), len(matrix[0])
    path = []

    def dfs(row, col):
        """
        This function should traverse the matrix and return False if coord is out of bounds or off limits
        Return True and add coord to path if in bounds
        """
        if (row == rows-1) and (col == columns-1):
            path.append((row,col))
            return True
        
        if (row > rows-1 or
            col > columns-1 or
            matrix[row][col] == 1):
            return False

        res = (dfs(row+1, col) or
               dfs(row, col+1))
        
        if res == True:
            path.append((row,col))
            return res
        
    if dfs(0,0):
      path.reverse()
      return print(f'Robot path through the matrix: {path}')
    return print('No path available')

# Testing:
if __name__ == "__main__":
    matrix = [[0,0,0,0,1,0],
              [1,1,0,1,1,0],
              [0,0,0,0,0,0],
              [0,0,0,0,1,0],
              [1,0,0,0,1,0],
              [0,1,0,0,1,0]]
    robot_in_grid(matrix)
    robot(matrix)
