def get_digit(num, digit):
    try:
        return int([char for char in str(abs(num))][::-1][digit])
    except IndexError:
        return 0


# print(get_digit(1242, 12))


def digit_count(num):
    return len(str(abs(num)))


def most_digits(l):
    return max([digit_count(num) for num in l])


def array_list():
    arr = []
    i = 0
    while i < 10:
        arr.append([])
        i += 1
    return arr


def radix_sort(l):
    max_digit_count = most_digits(l)
    for i in range(0, max_digit_count):
        bucket = array_list()
        for j in range(0, len(l)):
            digit = get_digit(l[j], i)
            bucket[digit].append(l[j])
            '''
            flattening the list.
            first for loop to flatten the original list.
            second for loop to flatten the individual 
            lists return by the original list.
            '''
        l = [n for num in bucket for n in num]
    return l


print(radix_sort([1, 12, 123, 53, 6432, 432, 4354, 53532]))
