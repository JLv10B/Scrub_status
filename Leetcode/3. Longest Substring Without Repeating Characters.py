"""
Given a string s, find the length of the longest substring without repeating characters

Input: string = "abcabcbb"
Output: 3, "abc"

Input: string = "pwwek"
Output: 3, "wek"

O(n), O(n)

Req:
- Because we need to look at a subset of an array we can use a sliding window approach
- As we use the sliding window approach we can use a set to store the unique char that have been seen
- Each time a char is added to the set we can update the length if needed
- To use a sliding window we will need 2 pointers 1 at the start of the window and 1 at the right/end of the window
- The start_index will start at 0 and stay until there is a repeat found if a repeated char is found
- The right_index will iterate through the array, if a repeated char is found,increment the start_index and remove letters until the repeated char is no longer in the set
- Return the length of the longest substring without repeated char
"""

def longest_substring(s):
    # Initiate substring_set, length, and start_index
    substring_set = set()
    length = 0
    start_index = 0

    # Use a for loop as the right_index of the sliding window and iterate through the string
    # If a repeated char is found then remove the starting letter and increment the start_index until the original repeated char is no longer in the set
    # Add the letter to the set and recalculate the length of the longest substring
    for right_index in range(len(s)):
        while s[right_index] in substring_set:
            substring_set.remove(s[start_index])
            start_index += 1
        substring_set.add(s[right_index])
        print(f'index = {right_index}, start = {start_index}, length = {length}, index-start+1 = {right_index-start_index+1}')
        length = max(length, right_index-start_index+1)

    return length

# Testing:
if __name__ == "__main__":
    s = 'pwwkew'
    print(longest_substring(s))
