"""
Ask:
Write a method to sort an array of strings so that all the anagrams are next to
each other

example
Input: [qwe, wer, ert, ewq, rew, tre]
Output: [qwe, ewq, wer, rew, ert, tre]

notes:
-Sort strings
-Compare strings
-Return an array of strings
-Given an array of strings and we want to find all the strings that have the same assortment of letters and sort them next
to each other

-Sort all the strings into their sorted letters and group them in a dictionary
-extend into new sorted array and return
"""
# Initiate {anagrams}
# For each word in [array]
# Sort letters and check {anagrams} if the sorted word is already a key
# If so then add unsorted word into value list, if not then create new key:value pair
# Create new [sorted_array] and extend {anagrams} values to create grouped array

def group_anagram(array):
    anagrams = {}
    for word in array:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)

    print(anagrams)

    sorted_array = []
    for values in anagrams.values():
        sorted_array.extend(values)

    return sorted_array
    
# Testing:
if __name__ == "__main__":
    
    
    array = ['qwe', 'wer', 'ert', 'ewq', 'rew', 'tre']
    print(group_anagram(array))