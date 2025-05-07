# Find the length of an array without using .length.

arr = [10, 20, 30, 40, 50]

count = 0

for _ in arr:
    count += 1

print(count)


# with while loop

arr = [1, 2, 10, 20, 30, 40, 50]
count = 0

try:
    while True:
        _ = arr[count]
        count += 1
except IndexError:
    pass

print(count)

# with recursion
def find_length(arr, index=0):
    try:
        _ = arr[index]
        return 1 + find_length(arr, index + 1)
    except IndexError:
        return 0
    
arr = [1, 3, 5, 6, 5, 4, 3,9]
print("lenght with recursion: ", find_length(arr))
