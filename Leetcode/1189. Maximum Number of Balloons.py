"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example:
Input: text = "nlaebolko"
Output: 1

Input: text = "loonbalxballpoon"
Output: 2

Req:
-Counter to track number of instances of the word ballon that can be formed
    -Incremented with each instance of balloon
-Instance of ballon is determined if enough letters are available
    -Letters can be out of order to need a way to track the letters
    -Dict?

Approach:
-Initiate counter and dict
-Store b,a,l,o,n in dict
-Find how many iterations of balloon are stored in dict
    -divide l and o by 2 because you need double to form balloon
"""

def max_number_balloon(text):
    letter_dict = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}

    for letter in text:
        if letter in letter_dict:
            letter_dict[letter] +=1

    letter_dict['l']//2
    letter_dict['o']//2

    return min(letter_dict.values())

# Testing:
if __name__ == "__main__":
    text = "nlaebolkoballoon"
    print(max_number_balloon(text))