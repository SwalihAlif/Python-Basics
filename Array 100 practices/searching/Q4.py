#Find the last occurrence of an element.
def find_last(arr, n):

    for i in range(len(arr)-1, -1, -1):
        if arr[i] == n:
            return f"{n} is in index: {i}"
    return f"{n} not in arr"


arr = [1, 2, 3, 4, 1, 2, 3, 4]
n = 3

print(find_last(arr, n))