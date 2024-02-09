"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into 
a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

Input: s = "catsandog", wordDict = ["sand","cats","dog","and","cat"]
Output: false

Input: s = "dadaddmade", wordDict = ["dade", "dad", "made", "add", "dam"]
Output: true

Notes:
-The question that we are looking to answer is can we use all the letters in s to create one or more works in 
wordDict
-Must keep the order or you can get a false positive from anagrams in wordDict

-We can iterate through each word in wordDict and see if any word starts at the beginning of string s
-If a word is found then start over and start at the end of the first found word
-Continue until no possible words are left, if there are unused letters then return False

"""
memo = {}
def word_break(s, wordDict, index):
    # Base cases:
    # if index in memo:
    #     return memo[index]
    if len(s) == 0:
        # memo[index] = True
        return True
    
    # Iterate through wordDict
    # For each word check if it's the prefix of s
    # If the word is found recheck wordDict to see if the word is the new segment's prefix
    for word in wordDict:
        print(f'word = {word}, s = {s}')
        if word in s[:len(word)]:
            # memo[index] = True
            if word_break(s[len(word):], wordDict, len(word)):
                return True

    return False
        
# Testing
if __name__ == "__main__":
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(word_break(s, wordDict,0))
