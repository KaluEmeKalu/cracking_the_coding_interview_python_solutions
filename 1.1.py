# Determine whether or not a given string contains no duplicate characters.

a = 'butterfly'
b  = 'investor'

def norepeat(string):
    b = set()
    for x in string:
        if x in b:
            return False
        else:
            b.add(x)        
    return True

print(norepeat(a))