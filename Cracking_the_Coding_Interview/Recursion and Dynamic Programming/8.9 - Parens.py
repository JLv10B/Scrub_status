"""
Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
of n pairs of parentheses.
EXAMPLE
Input: 3
Output: ( (() ) ) , (() ()) , (()) (), () (()) , ()()()

Input: 0
Output:

Input: 1
Output: ()

Input: 2
Output: ()(), (())

Approach:
-knowing how many parenthesis are available we know how many indexes need to be filled
-Create a temp string with ['*']*n*2 to as place holder
-Replace each index with ( or ) then check if it's valid
    -Can't use an empty list and append because it will affect the temp string for future recrusions 
    even if it's invalid
-If it's valid then we continue, if it's not then we end without saving that permutation
-When we run out of parenthesis we save that parenthesis to results
"""
def gen_parens(n):
    string_array = ['*']*n*2
    result = []
    parenthesis(result, n, n, string_array, 0)
    return result

def parenthesis(result, left, right, string_array, index):
    """result: list of permutations
    left: int count for remaining left parenthesis decrements with each addition of left parenthesis
    right: int count for remaining right parenthesis decrements with each addition of right parenthesis
    string_array: list of parenthesis before joining into string
    index: index of the target position increments with each recursion
    """
    # 2 base case
    # If we start an invalid permutation we return without saving
    # If we don't have any left or right parenthesis left then we join and append to result
    print(f'Left: {left}, Right: {right}, String array: {string_array}')

    if left < 0 or right < left:
        return

    if left == 0 and right == 0:
        element = ''.join(string_array)
        result.append(element)
        return result
    
    # Place ( or ) at current index then recurse to check if it is valid or if it's at end of string
    else:
        string_array[index] = '('
        parenthesis(result, left-1, right, string_array, index + 1)

        string_array[index] = ')'
        parenthesis(result, left, right-1, string_array, index + 1)

        
# Testing:

if __name__ == "__main__":
    print(gen_parens(0))
    print(gen_parens(1))
    print(gen_parens(2))
    print(gen_parens(3))