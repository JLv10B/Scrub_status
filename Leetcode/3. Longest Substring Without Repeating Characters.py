"""
Given a string s, find the length of the longest substring without repeating characters

Input: string = "abcabcbb"
Output: 3, "abc"

Input: string = "pwwek"
Output: 3, "wek"

O(n), O(n)
"""

def longest_substring(s):
    """
    -Iterate throug the string counting the length of each substring until repeated character is identified
    -Save the longest substring length then repeat until end of string is reached
    """
    # Initiate substring_set and substring_length
    substring_set = set()
    length = 0
    start = 0

    for index in range(len(s)):
        while s[index] in substring_set:
            substring_set.remove(s[index])
            start += 1
        substring_set.add(s[index])
        print(f'index = {index}, start = {start}, length = {length}, index-start+1 = {index-start+1}')
        length = max(length, index-start+1)

    return length

# Testing:
if __name__ == "__main__":
    s = 'pwwkew'
    print(longest_substring(s))
