# Determine whether the edit distance between two strings is less than 2.

def one_edit_away(str1, str2):
    list1 = list(str1)
    list2 = list(str2)



    no_changes_made = True
    if len(list1) == len(list2):
        for index, letter in enumerate(list1):
            if letter != list2[index] and no_changes_made:
                list2[index] = letter
                no_changes_made = False



    elif len(list1) - len(list2) == 1:
        bigger = max(list1, list2)
        smaller = min(list1, list2)
        for index, letter in enumerate(bigger):
            if index == len(bigger) - 1:
                smaller.append(letter)


            if letter != smaller[index] and no_changes_made:
                smaller.insert(index, letter)
                no_changes_made = False
        list1, list2 = bigger, smaller
    else:
        return False
    return list1 == list2


words1 = ['pale', 'ple']
words2 = ['pales', 'pale']
words3 = ['pale', 'bale']
words4 = ['pale', 'bake']
ans = one_edit_away(*words4)
print(ans)
