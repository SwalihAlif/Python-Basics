def increaseLast(digits):
    n = len(digits)

    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    return [1] + digits

    

arr = [1, 2, 3]
arr1 = [1, 2, 9]
arr2 = [9, 9, 9]

print(increaseLast(arr))
print(increaseLast(arr1))
print(increaseLast(arr2))
