# Given two strings, write a method to decide if one is a permutation of the other. 

a = 'robot', 'botor'
b = ['singer', 'player']

def make_d(str):
    d = {}
    for s in str:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    return d

def is_perm(str1, str2):
    d1 = make_d(str1)
    d2 = make_d(str2)
    return d1 == d2

print(is_perm(*a))
