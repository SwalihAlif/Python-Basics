# Find maximum of lst

def maximum_lst(lst):
    maximum = lst[0]

    for i in lst:
        if i > maximum:
            maximum = i

    return maximum

lst = [-10, -5, -2, -3, -4]

print(maximum_lst(lst))