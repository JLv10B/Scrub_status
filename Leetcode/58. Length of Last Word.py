"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

example:
Input: s = "Hello World"
Output: 5

Input: s = "   fly me   to   the moon  "
Output: 4

Req:
-Find the length of the last word in the string
    -Find the last word in the string
    -Find the length and return

Approach:
-Convert string into list of words, stripping all spaces
-return len() of last word
"""

def length_of_last_word(s):
    words = s.strip().split()
    if len(words) == 0:
        return 0
    return len(words[-1])

#Testing:
if __name__ == "__main__":
    s = "   fly me   to   the moon  "
    print(length_of_last_word(s))
