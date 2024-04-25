"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Req:
-Is s a subsequence of t?
    -do the letters in s exist in t and are they in the correct relative order

Approach:
-2 pointers
    -reference_pointer iterates through t
    -sub_pointer points at s and moves to the right if there is a match found between s & t
-at the end of the for loop if sub_pointer is > len(s) then return true
"""

def is_subsequence(s,t):
    sub_pointer = 0

    for i in range(len(t)):
        if t[i] == s[sub_pointer]:
            sub_pointer += 1
            print(sub_pointer)
    
    return sub_pointer == len(s)

# Testing:
if __name__ == "__main__":
    s = 'ace'
    t = 'abcde'
    print(is_subsequence(s,t))