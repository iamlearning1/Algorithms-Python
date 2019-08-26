def insertion_sort(arr):
    i = 1

    while i < len(arr):
        current = arr[i]
        j = i - 1
        while j > -1:
            if arr[j] > current:
                arr[j + 1] = arr[j]
                arr[j] = current
            j -= 1
        i += 1
    return arr


print(insertion_sort([2, 1, 9, 76, 4]))
