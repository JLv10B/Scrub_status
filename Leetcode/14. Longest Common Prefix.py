"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Req:
-Longest common prefix can't be longer than the shortest word

Approach:
-Sort the list using sort() method placing the longest potential prefix at the beginning
-Compare the first word and the last word
    -Only need to iterate through the first word as it's the longest potential prefix

"""

def longest_common_prefix(strs):
    strs.sort()

    first_word = strs[0]
    last_word = strs[-1]
    longest_prefix = ''

    for i in range(len(first_word)):
        if first_word[i] == last_word[i]:
            longest_prefix += first_word[i]
    return longest_prefix

# Testing:
if __name__ == "__main__":
    strs = ['abcd', 'abc']
    print(longest_common_prefix(strs))