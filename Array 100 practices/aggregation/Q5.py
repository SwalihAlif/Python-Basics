# find average of lst

def average(lst):
    total = 0
    count = 0

    for num in lst:
        total += num
        count += 1

    avg = total / count

    return avg

lst = [1, 2, 3, 4, 5]
print(average(lst))
