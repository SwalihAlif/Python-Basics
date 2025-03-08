def while_break(n, b):
    i = 1
    while i <= n:
        print(i)
        if i == b:
            break
        i += 1

n = 10
b = 6

while_break(n, b)