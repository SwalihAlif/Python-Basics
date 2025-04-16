# second largest and third largest

def third_largest(lst):

    largest = float('-inf')
    second = float('-inf')
    third = float('-inf')

    for num in lst:
        if num > largest:
            third = second
            second = largest
            largest = num
        
        elif num > second and num != largest:
            third = second
            second = num
        elif num > third and num != second and num != largest:
            third = num

    return third if third != float('-inf') else "nothing"

lst = [130, 130, 10]
print(third_largest(lst))
