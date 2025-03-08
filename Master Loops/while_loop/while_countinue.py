def while_countinue(n, c):
    i = 0
    while i < n:
        i += 1
        if i == c:
            continue
        print(i)

n = 10
c = 5


while_countinue(n, c)