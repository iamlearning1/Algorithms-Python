def pivot(arr, start, end):
    pivot = arr[start]
    swapIndex = start
    for i in range(start + 1, len(arr)):
        if pivot > arr[i]:
            swapIndex += 1
            arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
    arr[start], arr[swapIndex] = arr[swapIndex], arr[start]
    return swapIndex


def quick_sort(arr, start, end):
    if start < end:
        pivotIndex = pivot(arr, start, end)
        quick_sort(arr, start, pivotIndex - 1)
        quick_sort(arr, pivotIndex + 1, end)
    return arr


arr = [-100, 8, 2, 4, 6, 9, 1, 5, 3, 23, -5]
print(quick_sort(arr, 0, len(arr)))
