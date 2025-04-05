#Find the first occurrence of an element.

def first_occur(arr, n):
    try:
        return arr.index(n)
    except ValueError:
        return f"{n} not found in the list."
    

arr = [1, 2, 5, 3, 4, 5]
n = 20
print(first_occur(arr, n))