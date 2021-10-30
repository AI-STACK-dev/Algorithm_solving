# n = int(input())
# ary = []
# for _ in range(n):
#     ary.append(int(input()))
# ary.sort()
# sum_ = 0
# for i in range(1,n):
#     temp = ary[i-1]
#     temp += ary[i]
#     sum_ += temp
# print(sum_)


# N = int(input())

# candidates = [0] * N

# for i in range(N):
#     num = int(input())
#     candidates[i] = num
# candidates.sort()

# sumValue = candidates[0]
# sumValuelist = []
# for i in range(1,N):
#     num1, num2 = sumValue, candidates[i]
#     sumValue = num1 + num2
#     sumValuelist.append(sumValue)

# print(sum(sumValuelist))

import heapq

n = int(input())

# 힙(Heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힙(Heap)에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)