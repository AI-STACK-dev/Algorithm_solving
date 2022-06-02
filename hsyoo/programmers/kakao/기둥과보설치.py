# def check_g(x,y, g_list, b_list):
#     # if y == 0 or b_list[x-1][y] == 1 or g_list[x][y-1] == 1:
#     if y == 0 or b_list[x-1][y] == 1 or b_list[x][y] == 1 or g_list[x][y-1] == 1:
#         return True
#     else:
#         return False
# def check_b(x,y, g_list, b_list):
#     if g_list[x][y-1] == 1 or g_list[x+1][y-1] == 1 or (b_list[x-1][y] == 1 and b_list[x+1][y] == 1):
#         return True
#     else:
#         return False

# def solution(n, build_frame):
#     answer = [] # 내부에 x,y,a는 [x,y,a]형식으로 넣기
#     g_list = [[0]*(n+1) for _ in range(n+1)]
#     b_list = [[0]*(n+1) for _ in range(n+1)]
#     for case in build_frame:
#         x,y,a,b = case
#         # a - 기둥: 0, 보: 1
#         # b - 삭제: 0, 설치 : 1

#         if b == 1:
#             if a == 0:
#                 #기둥 체크
#                 result = check_g(x,y, g_list, b_list)
#             else:
#                 #보 체크
#                 result = check_b(x,y, g_list, b_list)
#             if result == True:
#                 answer.append([x,y,a])
#                 if a == 0:
#                     g_list[x][y] = 1
#                 else:
#                     b_list[x][y] = 1
#         else:
#             flag = True
#             if a == 0:
#                 g_list[x][y] = 0 
#             else:
#                 b_list[x][y] = 0
#             for item in answer:
#                 if item == [x,y,a]:
#                     continue
#                 x_prime, y_prime, a_prime = item
#                 if a_prime == 0:
#                     result = check_g(x_prime, y_prime, g_list, b_list)
#                 else:
#                     result = check_b(x_prime, y_prime, g_list, b_list)
#                 flag = flag and result
#             if flag == True:
#                 answer.remove([x,y,a])
#             else:
#                 if a == 0:
#                     g_list[x][y] = 1 
#                 else:
#                     b_list[x][y] = 1
#         # print(case, answer, result)
#     answer.sort()
#     return answer






def possible(answer):
    ## 기둥인 경우 -> 보인 경우
    for x,y,arch in answer:
        if arch == 0:
            if y == 0 or [x,y,1] in answer or [x-1,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        else:
            if [x,y-1,0] in answer or [x+1, y-1, 0] in answer or ([x-1,y,1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,arch, cmd = frame
        if cmd == 1:
            answer.append([x,y,arch])
            if not possible(answer):
                answer.remove([x,y,arch])
        else:
            answer.remove([x,y,arch])
            if not possible(answer):
                answer.append([x,y,arch])
    answer.sort()
    return answer


# def possible(answer):
#     for x, y, stuff in answer:
#         if stuff == 0:
#             if y ==0 or [x-1, y, 1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
#                 continue
#             return False
#         else:
#             if [x,y-1,0] in answer or [x+1, y-1, 0] in answer or ([x-1,y,1]in answer and [x+1,y,1] in answer):
#                 continue
#             return False
#     return True

# def solution(n, build_frame):
#     answer = []
#     for frame in build_frame:
#         x,y,stuff,operate = frame
#         if operate == 0:
#             answer.remove([x,y,stuff])
#             if not possible(answer):
#                 answer.append([x,y,stuff])
#         if operate == 1:
#             answer.append([x,y,stuff])
#             if not possible(answer):
#                 print(answer)
#                 answer.remove([x,y,stuff])
#     return sorted(answer)

# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	
# print(solution(5, build_frame))
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	
print(solution(5, build_frame))