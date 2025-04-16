# find minimum

def minimum_list(lst):

    minimum = lst[0]

    for num in lst:
        if num < minimum:
            minimum = num

    return minimum

lst = [1, 2, -1, 3, 4]

print(minimum_list(lst))