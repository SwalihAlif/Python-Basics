# #Must-Know Logic Problems
# Find unique elements in a list

def find_unique(lst):
    seen = set()
    result = []
    for i in lst:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result
nums = [1, 2, 3, 4, 2, 3, 4, 5]
print(find_unique(nums))

# Find duplicates in a list

# Find the most repeated element in a list

# Find the least repeated element in a list

# Count frequency of all elements in a list

# Check if two strings are anagrams

# Reverse a string or list without using built-in functions

# Check if a string is a palindrome

# Find the second largest and second smallest number

# Check if all characters in a string are unique

# Merge two sorted lists

# Find common elements in two lists

# Remove all occurrences of a specific element

# Flatten a nested list

# Rotate a list left or right by k steps

# Sort dictionary by keys or values

# Find all pairs that sum up to a target number

# Find missing number in a list of consecutive numbers

# Check if a number is a prime

# Generate Fibonacci sequence (up to n or n terms)