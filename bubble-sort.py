def bubble_sort(arr):
    i = len(arr)
    while i > 0:
        print(arr)
        no_swaps = True
        for j in range(0, i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                no_swaps = False
        i -= 1
        if (no_swaps):
            break
    return arr


print(bubble_sort([2, 54, 64, 12, 51, 89, 9]))
print(bubble_sort([2, 1, 3, 4, 5, 6, 9]))
