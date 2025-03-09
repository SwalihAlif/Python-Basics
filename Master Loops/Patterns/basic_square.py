for i in range(4):
    for j in range(4):
        print('*', end='')
    print()

print("\n")
# optimized
print(("*" * 5 + '\n') * 5, end="")