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
    bottom = len(matrix)-1
    right_border = len(matrix[0])-1
    path_list = [[(0,0)]]
    if robot_movement(matrix, path_list):
        return print(f'Robot path through the matrix: {path_list}')
    else:
        return print(f'Path list: {path_list}')

def robot_movement(matrix, path_list):
    print(f'Path list: {path_list}')
    bottom = len(matrix)-1
    right_border = len(matrix[0])-1
    path = path_list.pop(0)
    print(f'Path: {path}')
    row = path[-1][0]
    column = path[-1][1]
    # Base case is if coordinate is out of bounds or hits a dead end we terminate that path
    if (row + 1) > bottom or matrix[row+1][column] == 1:
        # print(f'base 1 false {row + 1} > {bottom} or {matrix[row+1][column]} = 1')
        if (column + 1) > right_border or matrix[row][column+1] == 1:
            # print(f'base 2 false {column + 1} > {right_border} or {matrix[row][column+1]} = 1')
            return False
        else:
            new_path = path.copy()
            new_path.append((row, column+1))
            path_list.append(new_path)
            print(path_list)
            print(f'Path_list after right check: {path_list}')
            robot_movement(matrix, path_list)
            return True
    # Checks path downwards
    elif matrix[row+1][column] == 0:
        new_path = path.copy()
        new_path.append((row+1, column))
        path_list.append(new_path)
        print(path_list)
        print(f'Path_list after down check: {path_list}')
        robot_movement(matrix, path_list)
        return True
    # return False



# Testing:
if __name__ == "__main__":
    matrix = [[0,0,0,0,1,0],
              [1,1,0,1,1,0],
              [0,0,0,0,0,0],
              [0,0,0,0,1,0],
              [1,0,0,0,1,0],
              [0,1,0,0,1,0]]
    robot_in_grid(matrix)
