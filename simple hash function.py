import random ,string

character=8

def hash_fun(strs):
    seed=0
    str_hash=''
    for i,c in enumerate(strs):
        seed += ord(c)* i + 42
        
    random.seed(seed)
    for x in range(character):
        str_hash+=random.choice(string.hexdigits[:16])
    return str_hash

print(hash_fun('hi'))
