# sum of elements in odd indices

def sum_odd_ind(lst):

    sum_odd = 0

    for i in range(len(lst)):
        if i % 2 != 0:
            sum_odd += lst[i]

    return sum_odd


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_odd_ind(arr))
