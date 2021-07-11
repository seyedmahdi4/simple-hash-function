import random ,string

character=8

def hash_fun(strs):
    seed=0
    str_hash=''
    for s in strs:
        seed += ord(s)* strs.index(s)+42
    random.seed(seed)
    for x in range(character):
        str_hash+=random.choice(string.hexdigits[:16])
    return str_hash

#hash_fun('hi') --> 'f843c001'
