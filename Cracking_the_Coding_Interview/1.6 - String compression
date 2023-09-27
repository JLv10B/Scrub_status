"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Input:
s = 'aabcccccaaa'
s = 'a'

Output:
s = 'a2b1c5a3'
s = 'a'

"""
# Initiate count variable to hold consecutive letter count, default set as 1 
# Intiate [new_string] to hold output before turning into string, set new_string[0] = s[0]
# Initiated 2 pointers: head(points to first instance of letter), tail(points to the letter being compaired to head)
# If head == tail: 
# Increment count variable and move tail pointer +1
# If head != tail: 
# Append str(count) to [new_string], append to [new_string], move head pointer to tail, and reset count to 1
# Once tail reaches end of string end loop and append str(count) to [new_string]
# Compare lengths of s vs [new_string], return the shorter string

def stringCompression(s):
    count = 1
    new_string = [s[0]]
    head = 0
    for tail in range(1, len(s)):
        if s[head] == s[tail]:
            count += 1
        else:
            new_string.append(str(count))
            new_string.append(s[tail])
            count = 1
            head = tail
    new_string.append(str(count))
    # print('new string:', new_string)
    # print('length of new string:', len(new_string))
    # print('length of old string:', len(s))

    if len(new_string) < len(s):    
        print(''.join(new_string))
    else:
        print(s)
    
    
if __name__ == '__main__':
    s = 'abbaaacccc'
    stringCompression(s)
