# find the product

def product(arr):

    prod = 1
    for i in arr:
        prod *= i

    return prod


arr = [1, 2, 3, 4, 5]
print(product(arr))
