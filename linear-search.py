def linear_search(nums, search):
    index = -1
    for num in nums:
        index += 1
        if num is search:
            return index
    return -1


print(linear_search([10, 15, 20, 25, 30], 30))
print(linear_search([1, 15, 6, 25, 8, 8], 8))
