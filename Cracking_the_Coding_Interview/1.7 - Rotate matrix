"""
 Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

Input:
[1 2 3]
[4 5 6]
[7 8 9]

Output:
[7 4 1]
[8 5 2]
[9 6 3]
"""

def rotateMatrix(matrix):
    
    print('original:', *matrix, sep = '\n')

    top = []
    for layer in range(int(len(matrix)/2)): # Layer = how many levels from top to middle of matrix, len(matrix)/2. Starts from outside then moves inwards
        for index in range(len(matrix)-1-(layer*2)): # Iterates across the top row of the layer left to right, skips the layers that have already been rotated
            top.append(matrix[layer][index+layer]) # Store value in top row moving left to right
            # print('top:', top)
            # print(f'rotate layer {layer}:', *matrix, sep = '\n')
            matrix[layer][index+layer] = matrix[len(matrix)-index-1-layer][layer] # Replaces top row value with left column value, moves bottom up
            matrix[len(matrix)-index-1-layer][layer] = matrix[len(matrix)-1-layer][-1-index-layer] # Replaces left value with bottom value, moves right to left
            matrix[len(matrix)-1-layer][-1-index-layer] = matrix[layer+index][-1-layer] # Replaces bottom value with right column value, moves top down
            matrix[layer+index][-1-layer] = top.pop(0) # Replaces right column value with stored top value

        # print(f'rotate layer {layer}:', *matrix, sep = '\n')

    print('rotate 90 complete:', *matrix, sep = '\n')

if __name__ == '__main__':
    matrix = [[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]]
    # matrix = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    # matrix = [[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0], [1,2,3,4,5,6,7,8,9,0], [1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0]]
    # matrix = [[0, 0, 0, 0],[0, 1, 2, 0],[0, 3, 4, 0],[0, 0, 0, 0]]
    rotateMatrix(matrix)