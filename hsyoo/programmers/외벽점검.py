# def solution(n, weak, dist):
#     answer = 0
#     ary = [False] * n
#     for idx in weak:
#         ary[idx] = True
#     ary += ary
#     flag = 0
#     start, end = 0,0
#     while True:
#         print(ary[:12], start, end)
#         if sum(ary[:n]) == 0:
#             break
#         elif len(dist) == 0:
#             flag = 1
#             break
#         else:
#             step = dist.pop()
#             answer += 1
#             max_ = -1
#             for i in range(n):
#                 temp = sum(ary[i:i+step+1])
#                 if temp > max_:
#                     max_ = temp
#                     start = i
#                     end = i+step+1
#             for i in range(start, end):
#                 ary[i%n] = False
#         # print(dist)
    
#     if flag == 1:
#         return -1
#     else:
#         return answer

from itertools import permutations

def solution(n, weak, dist):
    L = len(weak)
    cand = []
    weak_point = weak + [w + n for w in weak]
    
    for i, start in enumerate(weak):
        for friends in permutations(dist):
            count = 1
            position = start
            for friend in friends:
                position += friend
                print(position, weak_point[i+L-1])


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10]	,[3, 5, 7]))