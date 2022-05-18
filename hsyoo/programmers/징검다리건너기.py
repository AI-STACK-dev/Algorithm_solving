# import heapq

# def solution(stones, k):
#     answer = 0
#     heap = []
#     ary = []
#     for idx, value in enumerate(stones):
#         heapq.heappush(heap, (value, idx))
#     prev = 0
#     while heap:
#         value, idx = heapq.heappop(heap)
#         ary.append(idx)
#         while len(heap) > 0 and value == heap[0][0]:
#             ary.append(heapq.heappop(heap)[1])
#         answer += (value - prev)
#         n = len(ary)
#         ary.sort()
#         for i in range(n-k+1):
#             # print(3442432)
#             if ary[i+k-1] - ary[i] == k-1:
#                 return answer
#         prev = value
#         # print(heap, ary, answer)
#     return answer

def solution(stones, k):
    left = 1
    right = int(2e9)
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))