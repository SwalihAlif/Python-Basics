# sum of the elements in even indices

def sum_eve_ind(lst):
    sum_eve = 0

    for i in range(len(lst)):
        if i % 2 == 0:
            sum_eve += lst[i]

    return sum_eve


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_eve_ind(arr))