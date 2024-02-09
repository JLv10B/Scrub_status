"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the 
reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different 
from "06".

Given a string s containing only digits, return the number of ways to decode it.
"""
def decode_variation_count(s):
    """
    -Given string s return count of number of ways to decode the digits into letters
    -
    
    Input: s = '11106'
    Output: 2, ('1 1 10 6', '11 10 6')
    
    Input: s = '3579090'
    Output: 0

    Input: s = '226'

             2
      2_     |    22
2_2_6 | 2_26      | 22_6

dp(0) == dp(1) + dp(2) == 2 + 1 == 3
dp(1) == dp(2) + dp(3) == 1 + 1 == 2
dp(2) == dp(3) == 1
dp(3) == 1

dp(0) == dp(1) + dp(2) == 1 + 1 == 2
dp(1) == dp(2) + dp(3) == 1 + 0 == 1
dp(2) == dp(3) + dp(4) == 0 + 1 == 1
dp(3) == 0
dp(4) == dp(5) == 1
dp(5) == 1
    """
    memo = {}
    for i in range(len(s)-1):
        memo[i] = decode_string_at_index(i, s)
    return print(memo[0])

def decode_string_at_index(i, string):
    # Base cases
    if i >= len(string):
        return 1
    elif string[i] == '0':
        return 0

    # If i is not the last index in the string and [i:i+2] is a valid integer (<=26) then we look at
    # i+1 and i+2
    if (i < len(string)-1) and (int(string[i:i+2]) <= 26):
        return decode_string_at_index(i+1, string) + decode_string_at_index(i+2, string)
    else:
        return decode_string_at_index(i+1, string)

# Testing:
if __name__ == "__main__":
    s = '226'
    decode_variation_count(s)
    
        
    

    