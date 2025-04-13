# Find the sum of all elements in an array.
# not to use sum()

def sum_arr(arr):
    total = 0

    for i in arr:
        total += i
    return total

lst = [1, 2, 3, 4, 5]
print(sum_arr(lst))