"""
Write a method to compute all permutations of a string of unique characters.

perm_wo_dup('c')
Output: ['c']

perm_wo_dup('bc')
b + perm_wo_dup(c) = 
Output: ['bc', 'cb']

perm_wo_dup('abc')
a + perm_wo_dup(bc) = 
    a + [bc, cb]
b + perm_wo_dup(ca) =
    b + [ca, ac]
c + perm_wo_dup(ab) =
    c + [ab, ba]
Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

step:
-take one letter and add all permutations of the remaining letters to it
-
"""
# def perms_wo_dups(word):
#     """
#     perms_wo_dups(abc)
#         pi(,abc,r)
#             index 0 = pi(a,bc,r)
#             index 1 = pi(b,ac,r)
#             index 2 = pi(c,ab,r)
#                 index 0 = pi(ca,b,r)
#                     index 0 = pi(abc,,r)
#                         r=[abc]
                
#                 index 1 = pi(cb,a,r)
#                     index 0 = pi(cba,,r)
#                         r=[abc,cba]
#     """
#     result = []
#     perms_inner('', word, result)
#     return result


# def perms_inner(prefix, suffix, result):
#     if len(suffix) == 0:
#         result.append(prefix)
#         return result
    
#     for index in range(len(suffix)):
#         letter = suffix[index]
#         before = suffix[:index]
#         after = suffix[index+1:]
#         perms_inner(prefix+letter, before+after, result)

def perms_wo_dups(letters):
    """
    pwd(ab)
        index = 0 pwd(b)
            perms = []
            r = [b]
        perms = [b]
        r=[ab]

        index = 1 pwd(a)
            perms = []
            r = [a]
        perms = [a]
        r=[ba]
    """
    result = []

    if len(letters) == 0:
        result.append('')
        return result
    
    for index in range(len(letters)):
        letter = letters[index]
        before = letters[:index]
        after = letters[index+1:]
        permutations = perms_wo_dups(before+after)
        for perm in permutations:
            result.append(letter + perm)
    
    return result


# Testing:

if __name__ == "__main__":
    word = 'abc'
    print(perms_wo_dups(word))

        
        
    

