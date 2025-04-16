# Difference between minimum and maximum

def diff_min_max(lst):

    minimum = lst[0]
    maximum = lst[0]

    for num in lst:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    diff = maximum - minimum

    return diff

lst = [1, 2, 3, 4, 50]
print(diff_min_max(lst))