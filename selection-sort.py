def selection_sort(arr):
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if (arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
    return arr


print(selection_sort([31, 17, 1, 7, 34, 13]))
