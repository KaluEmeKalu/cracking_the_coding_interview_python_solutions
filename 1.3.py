# Write a method to replace all spaces in a string with %20. 

a = "Mr Eke Agbai"

def urlify1(string):
    my_list = []

    for s in string:
        if s == " ":
            my_list.append("%20")
        else:
            my_list.append(s)
    return "".join(my_list)


def urlify2(string):
    return string.strip().replace(' ', '%20')
print(urlify2(a))