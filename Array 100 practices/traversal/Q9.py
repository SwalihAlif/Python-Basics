# Replace all occurrences of a given element with another value.

def change_all_occurances(lst, old_value, new_value):
    for i in range(len(lst)):
        if lst[i] == old_value:
            lst[i] = new_value
    return lst
        
        
arr = [1, 2, 30, 4, 5, 30, 6, 30]
print(change_all_occurances(arr, 30, 75))