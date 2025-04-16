# Find the product of the list

def product(lst):
    pr = 1
    for i in lst:
        pr *= i

    return pr

lst = [1, 2, 3, 4, 5]
print(product(lst))