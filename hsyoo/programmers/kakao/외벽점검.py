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

# from itertools import permutations

# def solution(n, weak, dist):
#     length = len(weak)
#     for i in range(length):
#         weak.append(weak[i]+n)
#     answer = len(dist) + 1
#     for start in range(length):
#         for friends in list(permutations(dist, len(dist))):
#             count = 1
#             # 해당 친구가 점검할 수 있는 마지막 위치 
#             position = weak[start] + friends[count - 1]
#             # 시작점부터 모든 취약 지점을 확인
#             for index in range(start, start + length):
#                 # 점검할 수 있는 위치를 벗어나는 경우
#                 if position < weak[index]:
#                     count += 1
#                     # 더 투입이 불가능하다면 종료
#                     if count > len(dist):
#                         break
#                     position = weak[index] + friends[count - 1]
#             answer = min(answer, count)
#     if answer > len(dist):
#         return -1
#     return answer






from itertools import permutations
def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(n + weak[i])
    answer = len(dist) + 1
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    else:
        return answer
    













print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10]	,[3, 5, 7]))