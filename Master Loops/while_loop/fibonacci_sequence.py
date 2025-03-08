def fibonacci_sequence(a, b):
    while b < 50:
        print(b, end=" ")
        a, b = b, a+b

a = 0
b = 1

fibonacci_sequence(a, b)