"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

ex.
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
ex.
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

req:
- Return the number of islands -> counter
- Any '1's that are connected horz or vert are considered the same island
- Once we find borders of an island (no longer finding any adjacent '1's) we increment the counter

count_islands(grid): This function counts the number of islands found
- Initialize (visted) as cache and counter = 0
- Iterates through the grid, if coord is not in visited use find_island_boders(grid, row, col, visited) and increment counterj
- return counter

find_island_boders(grid, row, col, visited): This function find the borders of the island and returns visited nodes
- Edgecases:
    -If coord is out of bounds then return
    -If coord is in visited the return
- Place the given node in visited
- If node is '0' return
- If node is '1' recurse up, left, right, down
- return visited

Time: O(n)
Space: O(n+m)

"""
def count_islands(grid):
    visited = set()
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited and grid[row][col] == '0':
                    visited.add((row,col))
            elif (row, col) not in visited and grid[row][col] == '1':
                find_island_borders(grid, row, col, visited)
                count += 1
    
    return count

def find_island_borders(grid, row, col, visited):
    # Basecase: out of bounds or already been visited
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or ((row,col) in visited):
        return
    
    visited.add((row,col))

    if grid[row][col] == '0':
        return visited
    elif grid[row][col] == '1':
        find_island_borders(grid, row+1, col, visited)
        find_island_borders(grid, row-1, col, visited)
        find_island_borders(grid, row, col+1, visited)
        find_island_borders(grid, row, col-1, visited)
        return visited
        

# Testing:
if __name__ == "__main__":
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    print(count_islands(grid))