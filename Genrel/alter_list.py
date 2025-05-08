# output should be [30, 10, 20, 40, 50]

lis = [10, 20, 30, 40, 50]

a, b, c, *rest = lis

new = [c, b, a] + rest

print(new)