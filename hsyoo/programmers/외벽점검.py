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
    weak_length = len(weak)
    for i in range(weak_length):
        weak.append(weak[i] + n)
    print(weak)
    answer = len(dist)+1
    for i in range(weak_length):
        start_point = [weak[j] for j in range(i, i+weak_length)]
        print(start_point)
        permute = permutations(dist, len(dist))
        for order in permute:
            friend_idx, friend_count = 0, 1
            possible_check_length = start_point[0] + order[friend_idx]
            for idx in range(weak_length):
                if start_point[idx] > possible_check_length:
                    friend_count += 1
                    if friend_count > len(order):
                        break
                    friend_idx += 1
                    possible_check_length = order[friend_idx] + start_point[idx]
            answer = min(answer, friend_count)
    if answer > len(dist):
        return -1
    else:
        return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10]	,[3, 5, 7]))