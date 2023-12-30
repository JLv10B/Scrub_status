"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Notes:
-Brute force: sort the list then iterate through the list to find the longest consecutive elements sequence

-Improved method:
-We need to find all the sequences the most efficient way possible so we can find the longest one
-Take values and put them in (num_set) so as we search it takes O(1) instead of iterating through the full list
-longest_sequence = holds length of longest sequence found
-sequences = {start of sequence : length of sequence}
-Iterate through nums and search through (num_set) to see if there are any numbers that are (n-1)
-length = length of current sequence
-If not, this indicates that n is the start of a sequence
-Once we have found the beginning of a sequence then we can search(num_set) for the next number in the sequence
-If found then length += 1 and look for the next one
-Once end of sequence is found store in {sequences}
-if length > longest_sequence then update longest_sequence
"""

def longest_sequence(nums):
    num_set = set(nums)
    longest_sequence = 1
    sequences = {}

    for n in nums:
        length = 1
        if n not in sequences:
            if n-1 not in num_set:
                while n+length in num_set:
                    length += 1
                longest_sequence = max(length, longest_sequence)
            sequences[n] = length
            
    print (sequences)
    return print(longest_sequence)

# Testing:

if __name__ == "__main__":
    # nums = [100,4,200,1,3,2]
    nums = [0,3,7,2,5,8,4,6,0,1]
    longest_sequence(nums)

