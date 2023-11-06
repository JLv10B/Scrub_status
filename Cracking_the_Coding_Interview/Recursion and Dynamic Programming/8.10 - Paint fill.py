"""
Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.

Input:
screen = [[0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0]]
point = (1,2)
new_color = 5

Output:
screen = [[0,0,0,0,0,0],
          [0,0,5,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0]]

screen = [[0,5,5,5,0,0],
          [0,5,5,5,0,0],
          [0,5,5,5,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0]]
...

"""
def paint_fill(screen, point, new_color):
    """
    -find the color at the point -> set to old_color 
    -run helper function to check adjacent coords for old_color
    -Initiate {visisted} -> row:col to store visited coords
    """
    row = point[0]
    col = point[1]
    bottom = len(screen)-1
    right_border = len(screen[0])-1
    old_color = screen[row][col]
    visited = {}
    if row < 0 or row > bottom or col < 0 or col > right_border:
        return print('Point not on screen')
    
    helper(screen, row, col, old_color, new_color, visited)
    for row in range(len(screen)):
        print(screen[row])
    return

def helper(screen, row, col, old_color, new_color, visited):
    """
    -use helper function to replace point with new_color
    -check all adjacent coords and if they are set to the old_color then replace with new_color
    -add checked coords to visisted to avoid duplicate traversal
    -repeat until border is hit or if current color of the point is not the old_color
    """
    # 2 Base case:
    bottom = len(screen)-1
    right_border = len(screen[0])-1
    
    # If current_color is not old_color -> return
    current_color = screen[row][col]
    if current_color != old_color:
        return
    
    # If coord is in visisted -> return
    # If coord is not in visited add to visited 
    if row in visited:
        if col in visited[row]:
            return
        else:
            visited[row].append(col)
    else:
        visited[row] = [col]
    
        
    screen[row][col] = new_color
    # Keep all resursive calls on screen to decrease quantity of calls
    if row > 0:
        helper(screen, row-1, col, old_color, new_color, visited)
    if row < bottom:
        helper(screen, row+1, col, old_color, new_color, visited)
    if col > 0:
        helper(screen, row, col-1, old_color, new_color, visited)
    if col < right_border:
        helper(screen, row, col+1, old_color, new_color, visited)

# Testing:
if __name__ == "__main__":
    screen = [[2,2,2,2,2,2],
          [0,0,0,0,0,2],
          [0,0,0,0,0,2],
          [0,2,2,2,0,2],
          [0,0,0,0,0,2]]
    point = (-1,2)
    new_color = 5
    paint_fill(screen, point, new_color)
            
    