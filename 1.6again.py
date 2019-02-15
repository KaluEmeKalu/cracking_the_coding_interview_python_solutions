# String Compression: Input: aabccccaaa     Output: a2b1c5a3



def string_compression(string):
    if string == "":
        return ""


    current_letter = string[0]
    current_count = 1
    data = []
    for letter in string[1:]:
        if letter == current_letter:
            current_count += 1
        else:
            data.append(current_letter + str(current_count))
            current_count = 1
            current_letter = letter
    data.append(current_letter + str(string[current_count]))
    answer = "".join(data)

    return min(answer, string)



input1 = 'aabccccaaa'
ans = string_compression(input1)
print(ans)