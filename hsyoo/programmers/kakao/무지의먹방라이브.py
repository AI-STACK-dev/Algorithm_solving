# import heapq

# def solution(food_times, k):
#     answer = 0
#     n = len(food_times)
#     heap = []
#     check = [True] * n
#     for idx, time in enumerate(food_times):
#         heapq.heappush(heap, (time, idx))
    
#     while heap:
#         print(heap , k)
#         min_value, min_idx = heapq.heappop(heap)
#         if k >= (min_value * n):
#             k -= (min_value * n)
#             n -= 1
#             check[min_idx] = False
#             while heap[0][0] == min_value:
#                 print(heap[0][0])
#                 n-=1
#                 min_value, min_idx = heapq.heappop()
#                 check[min_idx] = False
#             heap = [(x[0] - min_value, x[1]) for x in heap]
#         else:
#             print(f"k : {k}")
#             idx = 0
#             while True:
#                 if check[idx] == True:
#                     idx += 1
#                     if idx == k:
#                          return idx
                
                
#     return -1

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    heap = []
    for idx,time in enumerate(food_times):
        heapq.heappush(heap, (time, idx+1))
    
    sum_ = 0
    pre = 0
    n = len(food_times)
    while sum_ + ((heap[0][0] - pre) * n) <= k:
        now = heapq.heappop(heap)[0]
        sum_ += (now - pre) * n
        n -= 1
        pre = now
    
    result = sorted(heap, key = lambda x : x[1])
    return result[(sum_ - k) * n][1]

print(solution([3,1,2], 5))