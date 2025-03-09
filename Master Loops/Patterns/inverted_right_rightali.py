def inverted_right_angle_right_align(n):
    for i in range(n, 0, -1):
        print(" " * (n-i) + "*" * i)


n = 5
inverted_right_angle_right_align(n)