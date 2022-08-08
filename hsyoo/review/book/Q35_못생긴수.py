# n = int(input())
# dp = [False, True]
# i = 2
# cnt = 1
# if n == 1:
#     print(1)
# else:
#     while cnt != n:
#         dp.append(0)
#         flag = False
#         if i % 2 == 0:
#             flag = True if dp[i//2] == True else False
#         elif i % 3 == 0:
#             flag = True if dp[i // 3] == True else False
#         elif i % 5 == 0:
#             flag = True if dp[i // 5] == True else False
#         else:
#             flag = False
#         if flag == True:
#             cnt += 1
#             dp[i] = True

#         i += 1 
#     print(i-1)

"""
Solution efficient
"""
n = int(input())
ugly = [0] * n
ugly[0] = 1
i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5
for l in range(1, n):
    ugly[l] = min(next2, next3, next5)
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5
print(ugly[n-1])