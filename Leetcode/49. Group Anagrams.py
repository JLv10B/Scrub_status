"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original letters exactly once.

Input: 
strs = ["eat","tea","tan","ate","nat","bat"]
Output: 
[["bat"],["nat","tan"],["ate","eat","tea"]]

Notes:
-anagrams = {}
-Sort each string, alphabetically by default
-If the sorted version is not in anagrams then anagrams[sorted_string] = [string]
-If it is in anagrams then append to [value]
-return array of key values
"""

def group_anagrams(array):
    anagrams = {}

    # Sorts strings into groups of anagrams
    # Should return {anagrams} with key:value 'abt': ['bat']
    for string in array:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagrams:
            anagrams[sorted_string] = [string]
        else:
            anagrams[sorted_string].append(string)

    # Return groups of anagrams in an array
    list = [x for x in anagrams.values()]
    return list

# Testing:
if __name__ == "__main__":
    array = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams(array))

    
