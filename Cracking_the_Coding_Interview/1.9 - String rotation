"""
Assume you have a method isSubstringwhich checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring(e.g.,"waterbottle"is a rotation of"erbottlewat").

Input: s1 = "waterbottle", s2 = "erbottlewat"

Output: True
all the letters must be the same, relative order should remain the same except for where it's rotated

Steps:
-Make sure that the strings are the same length
-Find where the 2 words match
-Continue to compare letters until there is a mismatch
"""

# if len(s1) != len(s2): False, break
# Initiate s1 & s2 pointers to 0
# Find the first match of s1 and s2
# Set pointers to matching indexes
# Compare s1 and s2
# When there's a match move both pointers += 1
# Continue to compare until there is a mismatch or until s1 == len(s1)
# if s2 == len(s2) set it to [0]

def isSubstring(s1, s2):
	if len(s1) != len(s2):
		print("False")
		return
	
	s1pointer = 0
	s2pointer = 0

	for index in range(len(s2)): # Find the first match of s1 and s2
		if s1[0] == s2[index]:
			s2pointer = index
		elif s1[0] != s2[index] and index == len(s2):
			print("False")
			return
	
	while s1pointer < len(s1):
		if s2pointer == len(s2): # If s2pointer reaches the end of s2 set it to [0]
			s2pointer = 0
		if s1[s1pointer] != s2[s2pointer]:
			print("False")
			return
		else:
			s1pointer += 1
			s2pointer += 1
			
	print("True")
			
if __name__ == "__main__":
	s1 = "hippostamp"
	s2 = "stamphippo"
	isSubstring(s1, s2)