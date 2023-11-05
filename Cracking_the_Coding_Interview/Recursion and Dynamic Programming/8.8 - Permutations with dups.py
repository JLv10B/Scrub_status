"""
Write a method to compute all permutations of a string whose characters are not necessarily unique. 
The list of permutations should not have duplicates.

perms(aabc) -> perms(a->2|b->1|c->1)
    a + perms(a->1|b->1|c->1)
        a + perms(b->1|c->1)
            b + perms(c->1)
            c + perms(b->1)
        b + perms(a->1|c->1)
            a + perms(c->1)
            c + perms(a->1)
        c + perms(a->1|b->1)
            a + perms(b->1)
            b + perms(a->1)
    b + perms(a->2|c->1)
        ...
    c + perms(a->2|b->1)
        ... 

"""

def perms(string):
    result = []
    map = build_freq_table(string)
    get_perms(map, '', len(string), result)
    return result


def build_freq_table(string):
    map = {}
    for letter in string:
        if letter not in map:
            map[letter] = 1
        else:
            map[letter] += 1
    # print(map)
    return map


def get_perms(map, prefix, remaining, result):
    if remaining == 0:
        result.append(prefix)
        return
    
    # print(f'map: {map}')
    for letter in map:
        count = map[letter]
        if count > 0:
            map[letter] -= 1 # The first time through this gets us a + perms(a->1|b->1|c->1)
            get_perms(map, prefix+letter, remaining-1, result)

            # Have to reset count to get
            # b + perms(a->2|c->1) and c + perms(a->2|b->1)
            # If map[letter] is not reset then the count for a will be 0
            map[letter] = count 
            

# Testing:

if __name__ == "__main__":
    word = 'aabc'
    print(perms(word))

        