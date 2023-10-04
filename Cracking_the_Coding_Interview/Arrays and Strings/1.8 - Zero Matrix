"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0

Input:
matrix = 
[1,1,1,0,1,1,1,1]
[1,1,1,1,1,1,1,1]
[1,1,0,1,1,1,1,1]
[1,1,1,1,1,0,1,1]
[1,1,1,1,1,1,1,1]

Output:
[0,0,0,0,0,0,0,0]
[1,1,0,0,1,0,1,1]
[0,0,0,0,0,0,0,0]
[0,0,0,0,0,0,0,0]
[1,1,0,0,1,0,1,1]

Steps:
-Identify location of 0s
    -linerally across the arrays
    -spiral
-When 0 is identified, if row/column has non-0 numbers then change to 0
    -want to avoid traversing the matrix multiple times


"""
# Approach 1: Brute force linear serach
# Initiate dictionary to hold column/index values of found 0s
# Iterate through each row
# Save index value of all found 0s
# Once end of row is reached, if a 0 was found replace each non-0 value with 0
# Once all rows are completed take list of columns and replace all non-0 values in each column with 0

def zeroMatrix(matrix):
    
    print("Original matrix:", *matrix, sep = '\n')
    
    columns = []
    rows = []
    for array in matrix: 
        for column in range(len(array)):
            if array[column] == 0:
                if column not in columns:
                    columns.append(column)
                if matrix.index(array) not in rows:
                    rows.append(matrix.index(array))

        # print('columns found:', columns,'rows found:', rows)

    for index in rows:
        for value in range(len(matrix[index])):
            # print('row:', matrix[index], 'value:', value)

            if matrix[index][value] != 0:
                matrix[index][value] = 0
    for index in columns:
        for row in range(len(matrix)):
            if matrix[row][index] != 0:
                matrix[row][index] = 0

    print("Zero'd matrix:", *matrix, sep = '\n')

if __name__ == '__main__':
    matrix =[[1,1,1,1,1,1,1,0],
             [1,1,1,1,1,1,1,1],
             [1,1,1,0,1,1,1,1],
             [1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1]]
    zeroMatrix(matrix)
