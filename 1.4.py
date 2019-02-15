# Given a string, write a function to check if it is a permutation of plaindrome.of

the_input = "Tact Coa"


def make_d(string):
    d = {}
    for letter in string:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    return d


def has_even_count_of_all_letters(string):
    d = make_d(string)

    for key, value in d.items():
        if value % 2 != 0:
            return False
    return True


def has_only_one_odd_count_of_letters(string):
    d = make_d(string)
    s = set()
    for key, value in d.items():
        if value % 2 != 0: # odd
            if key in s:
                return False
            else:
                s.add(key)
    return True
def is_plaindrome_perm(string):
    the_string = string.replace(" ", "")
    n = len(the_string)
    if n % 2 == 0:
        return has_even_count_of_all_letters(the_string)
    else:
        return has_only_one_odd_count_of_letters(the_string)



    return the_string


ans = is_plaindrome_perm(the_input)
print(ans)



