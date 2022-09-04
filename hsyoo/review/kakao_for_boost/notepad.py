# from collections import Counter
# def similarity(s1, s2):
#     inter_ = set(s1) & set(s2)
#     inter_ = list(inter_)
#     a = Counter(s1)
#     b = Counter(s2)
#     inter_value = 0
#     for case in inter_:
#         inter_value += min(a[case], b[case])
#     a.update(b)
#     union_value = sum(a.values()) - inter_value
#     return inter_value / union_value

# a.isalpha()
# b.isdigit()

# set1 & set2
# set1 | set2

# # update, add, remove
# c1 = Counter()
# c1.most_common(3)


# import math

# def is_prime(x):
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True

# print(is_prime(7))

# n = 5
# m = 3
# data = [1,2,3,2,5]

# count = 0
# interval_sum = 0
# end = 0
# for start in range(n):
#     print(start, end)
#     while interval_sum < m and end < n:
#         interval_sum += data[end]
#         end += 1
#     if interval_sum == m:
#         count += 1
#     interval_sum -= data[start]
# print(count)