"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

Input:
s = 'string'
t = 'gtirns'

Output = True

Notes:
-Create dictionary of letters for each string and compare.
-If dictionaries are the same then return true
"""

def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    
    s_letters = helper(s)
    t_letters = helper(t)
    
    if s_letters == t_letters:
        return True
    return False

def helper(string):
    anagram = {}
    for letter in string:
        if letter not in anagram:
            anagram[letter] = 1
        else:
            anagram[letter] += 1
    return anagram

# Testing:

if __name__ == "__main__":
    s = 'string'
    t = 'gnirts'
    print(valid_anagram(s,t))