"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its 
corresponding column number.

ex.
Input: columnTitle = 'AA' = 26 + 1
Output: 27

Input: columnTitle = 'AAA' = ((26^0) * 1) + ((26^1) * 1) + ((26^2) *1)
Output: 703

Input: columnTitle = 'BAA'
Output: 1379


-1-26 are defined
-If there is more than 1 letter in the string then
-Iterate through each letter and sum 26^index * corresponding int

"""
def column_number(columnTitle):
    # Initiate conversion_table for A-Z
    conversion_table = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
                        'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19,
                        'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    
    # If no values in string return 0
    if len(columnTitle) == 0:
        return None
    
    # Iterate through each index and return result
    result = 0
    i = len(columnTitle)-1
    for char in columnTitle:
        result += (26**i) * conversion_table[char]
        i -= 1

    return result

# Testing
if __name__ == "__main__":
    columnTitle = "BAA"
    print(column_number(columnTitle))