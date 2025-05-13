# #Must-Know Logic Problems
#1 Find unique elements in a list


# def find_unique(lst):
#     seen = set()
#     result = []
#     for i in lst:
#         if i not in seen:
#             result.append(i)
#             seen.add(i)
#     return result
# nums = [1, 2, 3, 4, 2, 3, 4, 5]
# print(find_unique(nums))
#--------------------------------------------------------
# def find_unique_1(lst):

#     freq = {}
#     result = []
#     for i in lst:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1
#         if freq[i] == 1:
#             result.append(i)
#     #return result # will print like the function before with seen()
#     return [x for x in result if freq[x] == 1]

# nums = [1, 2, 3, 4, 2, 3, 4, 5]
# print(find_unique_1(nums))
#-----------------------------------------------------------------------------
# from collections import Counter
# def find_unique_1(lst):
#     freq = Counter(lst)
#     unique = [k for k, v in freq.items() if v == 1]

#     return unique

# nums = [1, 2, 3, 4, 2, 3, 4, 5]
# print(find_unique_1(nums))

#===================================================================================
#2 Find duplicates in a list
# def find_duplicates(lst):
#     freq = {}
#     dupes = []
#     for i in lst:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1
        
#         if freq[i] > 1:
#             dupes.append(i)
#     return dupes

# nums = [1, 2, 3, 4, 2, 3, 4, 5, 2, 3, 3]
# print(find_duplicates(nums))
#----------------------------------------------------------------------------------------
# def find_duplicates_1(lst):
#     seen = set()
#     dupes = set()
#     for i in lst:
#         if i in seen:
#             dupes.add(i)
#         else:
#             seen.add(i)

#     return list(dupes)

# nums = [1, 2, 3, 4, 2, 3, 4, 5, 2, 3, 3]   
# print(find_duplicates_1(nums))
#------------------------------------------------------------------------------------
# from collections import Counter
# def find_dupes_counter(lst):
#     freq = Counter(lst)
#     dupes = [item for item, count in freq.items() if count > 1]
#     return dupes
# nums = [1, 2, 3, 4, 2, 3, 4, 5, 2, 3, 3]
# print(find_dupes_counter(nums))

#==============================================================================

#3 Find the most repeated element in a list
# def most_repeated(nums):
#     freq = {}
#     for i in nums:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1

#     most_key = None
#     most_count = 0
#     for key in freq:
#         if freq[key] > most_count:
#             most_count = freq[key]
#             most_key = key

#     return most_key, most_count

# nums = [2, 1, 2, 3, 2, 4, 3, 3, 3, 5, 2]
# a, b = most_repeated(nums)
# print(f"Most repeated num {a} is repeated {b} times.") #(only get any one of the most repeated)

#-------------------------------------------------------------------------------------------
# def most_repeated_to_arr(nums):
#     freq = {}
#     for num in nums:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1

#     most_count = 0
#     for count in freq.values():
#         if count > most_count:
#             most_count = count

#     result = []
#     for key in freq:
#         if freq[key] == most_count:
#             result.append(key)

#     return result, most_count

# nums = [2, 1, 2, 3, 2, 4, 3, 3, 3, 5, 2]
# lst, c = most_repeated_to_arr(nums)
# print(f"Most repeated nums {lst} which repeated {c} times.")
#===================================================================================
#4 Find the least repeated element in a list

# def least_repeated(nums):
#     freq = {}
#     for num in nums:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1
    
#     min_num = None
#     min_count = float('inf')
#     for key in freq:
#         if freq[key] < min_count:
#             min_count = freq[key]
#             min_num = key
    
#     return (min_num, min_count)

# nums = [2, 1, 2, 3, 2, 4, 3, 3, 3, 5, 1, 4, 2]
# a, b = least_repeated(nums)
# print(f"The least repeated: {a} is repeated only {b} times.")
#--------------------------------------------------------------------------------
# def least_repeated_lst(nums):
#     freq = {}
#     for num in nums:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1

#     min_count = float('inf')
#     for count in freq.values():
#         if count < min_count:
#             min_count = count
            

#     result = []
#     for key in freq:
#         if freq[key] == min_count:
#             result.append(key)

#     return result, min_count
# nums = [2, 1, 2, 3, 2, 4, 3, 3, 3, 5, 1, 'r', 2]
# lst, c = least_repeated_lst(nums)
# print(f"Least repeated: {lst} which repeated only {c} times.")
#--------------------------------------------------------------------------
# from collections import Counter
# def least_repeated_all(nums):
#     freq = Counter(nums)
#     min_count = min(freq.values())
#     least_repeated = [key for key, value in freq.items() if value == min_count]

#     return least_repeated, min_count

# nums = [2, 1, 2, 3, 2, 4, 3, 3, 3, 5, 1, 'r', 2]
# lst, c = least_repeated_all(nums)
# print(f"Least repeated: {lst} which repeated only {c} times.")

#===============================================================================

#5 Count frequency of all elements in a list
# def count_freq(nums):
#     freq = {}
#     for num in nums:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1
#     return freq

# nums = [2, 1, 2, 3, 2, 4, 3, 3, 3, 5, 1, 2]
# fq = count_freq(nums)
# sorted_fq = dict(sorted(fq.items()))
# print(sorted_fq)
#-----------------------------------------------------------------------------------------
# nums = [2, 1, 2, 3, 2, 4, 3, 3, 3, 5, 1, 2]
# from collections import Counter
# freq = Counter(nums)
# print(dict(sorted(freq.items())))

#===============================================================================================

#6 Check if two strings are anagrams

#7 Reverse a string or list without using built-in functions

#8 Check if a string is a palindrome

#9 Find the second largest and second smallest number

#10 Check if all characters in a string are unique
#========================================================================

# def is_unique(s):
#     seen = set()
#     for i in s:
#         if i in seen:
#             return False
#         seen.add(i)
#     return True

# st = "aeiou"
# print(is_unique(st))
#------------------------------------------------------------------
# def is_unique(s):
#     return len(s) == len(set(s))

# st = 'aeioeu'
# print(is_unique(st))
#===================================================================
#11 Merge two sorted lists

#12 Find common elements in two lists

# def find_common(nums1, nums2):
#     return [x for x in nums1 if x in nums2]

# n1 = [1, 2, 3, 4]
# n2 = [3, 4, 5, 6]

# print(find_common(n1, n2))
#===========================================================================
#13 Remove all occurrences of a specific element

# def remove_occr(nums, n):
#     new = []
#     for i in nums:
#         if i != n:
#             new.append(i)
#     return new

# nums = [2, 2, 3, 2, 2]
# n = 2

# print(remove_occr(nums, n))
#-----------------------------------------------------------------------------
# def remove_occure(nums, n):
#     i = 0
#     while i < len(nums):
#         if nums[i] == n:
#             nums.pop(i)
#         else:
#             i += 1

#     return nums
# nums = [2, 2, 3, 2, 2]
# n = 2
# print(remove_occure(nums, n))

# def remove_occure(nums,n):
#     return [x for x in nums if x != n]
# nums = [2, 2, 3, 2, 2]
# n = 2
# print(remove_occure(nums, n))
#=======================================================================================

#14 Flatten a nested list

# nested = [[1, 2], [3, 4], [5, 6], [7, 8]]
# flatten = []
# for arr in nested:
#     for num in arr:
#         flatten.append(num)

# print(nested)
# print(flatten)
#---------------------------------------------------------------------------------------
# nested = [[1, 2], [3, 4], [5, 6], [7, 8]]
# flatten = [num for arr in nested for num in arr]  
# print(flatten)
#---------------------------------------------------------------------------------------

#15 Rotate a list left or right by k steps

#16 Sort dictionary by keys or values

#17 Find all pairs that sum up to a target number

#18 Find missing number in a list of consecutive numbers

#19 Check if a number is a prime

#20 Generate Fibonacci sequence (up to n or n terms)