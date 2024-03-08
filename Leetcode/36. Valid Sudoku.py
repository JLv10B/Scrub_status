"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to 
the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Requirements:
- Each row does not have any repetition
- Each column does not have any repetition
- Each 3 x 3 sub box does not have any repetition
- Return true is all criteria are met, return false if any are false

- Iterate through the full list and record each number in coord_set as (row, element), (element, col), (row//3, col//3, element)
coord_set = []
- Return False if we get any repeats in row, any column, or any sub_box else return True

"""
def validate_sudoku(board):
    coord_check = set()

    for row in range(9):
        for col in range(9):
            val = board[row][col]
            if val != ".":
                coord_check.add((row, val))
                coord_check.add((val, col))
                coord_check.add((row//3, col//3, val))
    return len(coord_check) == len(set(coord_check))

# Testing:
if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    print(validate_sudoku(board))
