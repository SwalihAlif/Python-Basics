# 1. Find the index of an element in an array.

def index_of(arr, n):
    return arr.index(n)

arr = [1, 2, 3, 4, 5]
n = 4

print(f"Index of the {n} is {index_of(arr, n)}")