"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it

Input:
numRows = 3

Output:
[[1],[1,1],[1,2,1]]
"""
def pascal_triangle(numRows):
    """
    -Base case: numRows == 0, return []
    -Base case: numRows == 1, return [[1]]
    -Iterate through numRows constructing each row as you go
    -Return result

    Input:
    numRows = 3

    Output:
    [[1],[1,1],[1,2,1]]
    """
    # Base cases:
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    
    # Result recurses through numRows adding each row starting from [1]
    result = pascal_triangle(numRows-1)
    prev_row = result[-1]
    new_row = [1]

    for i in range(1, len(prev_row)):
        new_row.append(prev_row[i-1] + prev_row[i])

    new_row.append(1)
    result.append(new_row)
    return result

# Testing:
if __name__ == "__main__":
    numRows = 5
    print(pascal_triangle(numRows))