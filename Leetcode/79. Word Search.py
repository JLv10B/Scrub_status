"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally 
or vertically neighboring. The same letter cell may not be used more than once.

Input datastructure:
board = [[1,3,5,6,8],
         [4,5,6,3,4],
         [2,5,6,7,8],
         [3,5,7,8,0]]
number = [1,3,5,5,5,7,8]

path = ()

Output: True

Time: O(2n), 
space: O(n)
"""
def number_search(board, number):
    """
    - Find a possible starting location for the number by iterating through the board
    - Once found start a DFS

    """