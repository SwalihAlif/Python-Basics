#Check if an element exists in an array.

def is_exist(arr, n):
    return n in arr

arr = [1, 2, 3, 4, 5]
n = 1
if is_exist(arr, n):
    print(n, "is in the array")
else:
    print(n, "is not in the array")