"""
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true

Input: s = "race a car"
Output: false

Input: s = " "
Output: true

Approach:
-Brute force: 
-start pointer = starts at [0]
-end pointer = starts at [-1]
-before comparing we check if the charater is alphanumeric, if true then convert to lowercase
-we compare values and if they are the same then move the pointer 1 over
-loop is completed when start >= end (if start > end then they have overlapped)
"""

def valid_palindrome(string):
    if len(string) == 0:
        return True
    # Initiate end pointer
    end = len(string)-1

    # Check if pointers are pointing at alphanumeric characters
    # If true compare lowercase
    # If match then move pointers
    # End if start >= end
    for i in range(len(string)):
        if i >= end:
            return True
        
        if string[i].isalnum():
            while string[end].isalnum() is False:
                end -= 1
            
            # print(f'start: {string[i]}, end: {string[end]}')
            # print(f'start: {i}, end: {end}')
            if string[i].lower() != string[end].lower():
                return False
            end -= 1


# Testing:

if __name__ == "__main__":
    string = "A man, a plan, a canal: Panama"
    # string = "race a car"
    # string = ""


    print(valid_palindrome(string))