# sum of even

def sum_even(lst):

    sum_ev = 0

    for num in lst:
        if num % 2 == 0:
            sum_ev += num


    return sum_ev


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum_even(lst))