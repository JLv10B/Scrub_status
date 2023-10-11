"""
 There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

"""

# Initiate error variable to store error count
# Take the length of the longest string and subtract the length of the shorter string
# If there is >= 2 length difference then return false
# If the lengths of the strings are the same compare each letter
# If there's a mismatch increment the error count
# If the difference in length is == 1
# Take the longer string and compare each letter to the letters in the shorter string
# If there's a mismach then increment the error count but keep the shorter string's pointer stationary
# If the pointer reaches past the last letter in the shorter string -> missing the last letter, error += 1

def oneAway(string1, string2):
    errors = 0
    
    if abs(len(string1) - len(string2)) > 1:
        errors += abs(len(string1) - len(string2))

        # print('error count length:', errors)

    elif abs(len(string1) - len(string2)) == 1:
        long_string = max(string1, string2)
        short_string = min(string1, string2)
        pointer = 0
        for letter in long_string:
            if pointer == len(short_string):
                errors += 1
            elif letter == short_string[pointer]:
                pointer += 1
            elif letter != short_string[pointer]:
                errors += 1

        # print('error count:', errors)

    else:
        for index in range(len(string1)):
            if string1[index] != string2[index]:
                errors += 1

            # print('error count equal:', errors)
            # print('letter:', string2[index])


    if errors >= 2:
        print('False')
    else:
        print('True')
				

if __name__ == "__main__":
    string1 = 'pales'
    string2 = 'bakes'
    oneAway(string1, string2)