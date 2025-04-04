# Create a new array containing only the first half of an existing array.

def first_half(lst):
    
    half = len(lst) // 2
    new_lst = lst[:half]

        
    return new_lst
    
arr = [1, 2, 3, 4, 5, 6, 7, 8]

print(first_half(arr))