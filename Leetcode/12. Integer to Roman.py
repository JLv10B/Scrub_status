"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.


"""

def int_to_roman(num:int):
    """
    This function converts a given int into a str representing roman numerals

    example
    input: num = 1994
    output: "MCMXCIV"

    Approach:
    - Create a dictionary with integer to roman numeral conversions with exceptions {int:roman_numeral}
    - Create a list of all the same integers in the dictionary from largest to smallest
    - Iterate through the list and subtract from num, for each successful attempt add that value to result
    - return result as a string
    """
    
    int_roman_dict = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
    
    int_array = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    result = ""

    # Iterate through list and subtract from 
    for value in int_array:
        while num >= value:
            num -= value
            result += int_roman_dict[value]
    
    return result

# Testing:
if __name__ == "__main__":
    num = 1993
    print(int_to_roman(num))

