"""
You are given a string s and an integer k. You can choose any character of the string and change 
it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing 
the above operations.

ex.
Input: s = "ABAB", k = 2
Output: 4

Input: s = "AABABBA", k = 1
Output: 4

Req:
- Return the length of the longest substring containing the same letter
- We can find the length of a substring containing the same letter by staring at a letter and checking the
letters next to it. If the next letter is the same then continue to move to the right, each time the pointer
is moved to the right length_count is incremented. 
- If the next letter is different and change_count == k then set this as the potential_start. If change_count > 0 
then decrement k (this is counted as a change) and continue to move to the right. If k = 0 then check if 
the longest_substring needs to be updated and we start the process over at next_start.
- If the new starting point will be < longest_substring from the end of the string then return longest_substring

"""

def longest_repeating(s, k):
    # Initialize variables: 
    longest_substring = 0 # Output
    start = 0 # Starting location of the current substring
    potential_start = 0 # Starting location of the next substring

    while start < (len(s)-longest_substring):
        start = potential_start
        right = start
        length_count = 1 # Current length resets with each loop
        change_count = k # How many changes can be performed, resets with each loop
        while change_count >= 0 and right < (len(s)-1):
            if s[right+1] != s[start]:
                if change_count == 0:
                    change_count -= 1
                    break
                elif change_count == k:
                    potential_start = right+1
                    print(f'potential_start = {potential_start}')
                change_count -= 1
            length_count += 1
            right += 1
            print(f'right moved to {right}')
        longest_substring = max(longest_substring, length_count)
        print(f'updated longest substring to {longest_substring}')

    return longest_substring

# Testing:

if __name__ == "__main__":
    s = "ABAB"
    k = 0
    print(longest_repeating(s,k))

        

        