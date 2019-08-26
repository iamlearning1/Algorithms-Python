from math import floor


def merge(list1, list2):
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result


def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = floor(len(l) / 2)
    left = merge_sort(l[0:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)


print(merge_sort([1, 4, 10, 3, 89, 12, 3]))
