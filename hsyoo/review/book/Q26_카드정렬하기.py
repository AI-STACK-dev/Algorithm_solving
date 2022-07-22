# n = int(input())
# ary = []
# for _ in range(n):
#     ary.append(int(input()))
# ary.sort()

# if n == 1:
#     print(ary[-1])
# elif n == 2:
#     print(ary[0] + ary[1])
# else:
#     sum_temp = ary[0] + ary[1]
#     sum_all = sum_temp
#     for item in ary[2:]:
#         sum_temp += item
#         sum_all += sum_temp
#     print(sum_all)

import heapq
n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

answer= 0 
while len(q) != 1:
    num1 = heapq.heappop(q)
    num2 = heapq.heappop(q)
    sum_ = num1 + num2
    answer += sum_
    heapq.heappush(q, sum_)

print(answer)