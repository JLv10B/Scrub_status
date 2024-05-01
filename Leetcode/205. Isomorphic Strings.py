"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Req:
- All occurances of a char must be replaced
- No 2 char may map to the same index

Approach:
- Initialize map_s and map_t as empty lists
- Iterate through s and map_s.append() the first occurance of each letter
- Repeat for t
- If map_s == map_t return true, else return false


"""
def iso_strings(s,t):
    map_s = []
    map_t = []

    for i in s:
        map_s.append(s.index(i))
    for i in t:
        map_t.append(t.index(i))

    print(f'map_s = {map_s}, map_t = {map_t}')

    if map_s == map_t:
        return True
    return False

# Testing:
if __name__ == "__main__":
    s = "foo"
    t = "baa"
    print(iso_strings(s,t))