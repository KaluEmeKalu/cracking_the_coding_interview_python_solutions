# String Compression: Input: aabccccaaa     Output: a2b1c5a3


def string_compression(string):
    if not string:
        return ""
    current_letter = string[0]
    current_count = 1
    l = []
    for letter in string[1:]:
        if current_letter == letter:
            current_count += 1
        else:
            l.append(current_letter + str(current_count))
            current_letter = letter
            current_count = 1
    l.append(current_letter + str(current_count))
    ans = "".join(l)
    if ans > string:
        return string
    return ans

input1 = 'aabccccaaa'
ans = string_compression(input1)
print(ans)