# sum of odd numbers

def sum_of_odd(lst):

    sum_odd = 0
    for num in lst:
        if num % 2 == 1:
            sum_odd += num

    return sum_odd

# sum of multiples of 3
def sum_of_multi3(lst):
    return sum([num for num in lst if num % 3 == 0])


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_odd(lst))
print(sum_of_multi3(lst))