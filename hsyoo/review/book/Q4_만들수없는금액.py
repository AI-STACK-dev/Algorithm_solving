# from itertools import combinations

# n = int(input())
# ary = list(map(int, input().split()))
# comb_list = []
# for i in range(1, n+1):
#     comb_list.extend(list(combinations(ary, i)))
# comb_list = set(list(map(sum, comb_list)))
# print(comb_list)
# for i in range(1, 1000001):
#     if i not in comb_list:
#         break
# print(i)

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x
print(target)