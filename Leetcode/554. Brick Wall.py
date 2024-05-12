"""
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

example:
Input: wall = [[1,2,2,1],
               [3,1,2],
               [1,3,2],
               [2,4],
               [3,1,2],
               [1,3,1,1]]
Output: 2

Input: wall = [[1],[1],[1]]
Output: 3

Req:
-Draw a line that crossess the fewest bricks possible
    -Any width of wall has width-1 possible locations that we can draw a line
    -The width of a brick indicates at what location we can draw a line without crossing a brick
    -Create a dictionary that stores how many edges that a line would cross if drawn there
        -return the largest number and subtract from the total height of the wall

Approach:
-Initate edge_dict = {location: # of edges}
-Iterate through wall
    -Initiate width_adjustment to store the width of the bricks to the left
    -Iterate through each brick in the row excluding the last brick and increment key in dict
-return len(wall)-max(location_edge_dict.values(),default=0)
"""

def brick_wall(wall):
    location_edge_dict = {}

    for row in wall:
        width_adjustment = 0
        for width in row[:-1]:
            if width+width_adjustment not in location_edge_dict:
                location_edge_dict[width+width_adjustment] = 1
            else:
                location_edge_dict[width+width_adjustment] += 1
            width_adjustment += width

    return len(wall) - max(location_edge_dict.values(), default=0) # Set default to 0 in case location_edge_dict is empty

# Testing:
if __name__ == "__main__":
    wall = [[1,2,2,1],
               [3,1,2],
               [1,3,2],
               [2,4],
               [3,1,2],
               [1,3,1,1]]
    print(brick_wall(wall))
                

