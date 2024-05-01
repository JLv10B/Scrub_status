"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Req:
-if the words in s match the pattern then return True
-Convert s into pattern
    -convert s into list
    -create new string from list
    -create a comparison dictionary from new string to pattern
-Compare new string to pattern
"""

def word_pattern(pattern, s):
    word_list = s.split(' ')
    word_to_pattern_dict = {}

    for index in range(len(word_list)):
        if word_list[index] not in word_to_pattern_dict:
            word_to_pattern_dict[word_list[index]] = pattern[index]
        elif pattern[index] != word_to_pattern_dict[word_list[index]]:
            return False
        
    return True