from math import floor


def binary_search(arr, num):
    start = 0
    end = len(arr) - 1
    mid = floor((start + end) / 2)
    while num is not arr[mid] and start <= end:
        if num < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = floor((start + end) / 2)

    if arr[mid] is num:
        return mid
    else:
        return -1


print(binary_search([1, 2, 3, 4, 5], 1))
print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5], 5))
print(binary_search([1, 2, 3, 4, 5], 9))
