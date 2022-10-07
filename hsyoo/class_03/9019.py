# from collections import deque

# search_space = ['D', 'S', 'L', 'R']

# def D_func(n):
#     n = int(n)
#     n *= 2
#     n = n % 10000 if n > 9999 else n
#     return str(n)

# def S_func(n):
#     n = int(n)
#     n -= 1
#     n = 9999 if n == -1 else n
#     return str(n)

# def L_func(n):
#     # 문자열 입력으로 들어온다고 생각
#     s = n[1:] + n[:1]
#     return s

# def R_func(n):
#     s = n[-1:] + n[:-1]
#     return s

# def bfs(a, b, visited):
#     q = deque([])
#     a, b = str(a), str(b)
#     visited.add(a)
#     q.append((a, ''))
    
#     while q:
#         # print(q)
#         current, cmd = q.popleft()
#         if int(current) == int(b):
#             return cmd
#         for case in search_space:
#             if case == 'D':
#                 next = D_func(current)
#                 next_cmd = cmd + 'D'
#             elif case == 'S':
#                 next = S_func(current)
#                 next_cmd = cmd + 'S'
#             elif case == 'L':
#                 next = L_func(current)
#                 next_cmd = cmd + 'L'
#             else:
#                 next = R_func(current)
#                 next_cmd = cmd + 'R'
            
#             if next_cmd not in visited:
#                 q.append((next, next_cmd))
#                 visited.add(next_cmd)

# T = int(input())
# for _ in range(T):
#     a, b = map(int, input().split())
#     visited = set([])
#     cmd = bfs(a, b, visited)
#     print(cmd)

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A,B = map(int,input().split())
    q = deque()
    q.append((A,""))
    visit = [False] * 10000
    
    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == B:
            print(path)
            break
        
        # 1
        num2 = (2*num)%10000
        if not visit[num2]:
            q.append((num2,path+"D"))
            visit[num2] = True
        # 2
        num2 = (num-1)%10000
        if not visit[num2]:
            q.append((num2,path+"S"))
            visit[num2] = True
        # 3
        num2 = (10*num+(num//1000))%10000
        if not visit[num2]:
            q.append((num2,path+"L"))
            visit[num2] = True
            
        # 4
        num2 = (num//10+(num%10)*1000)%10000
        if not visit[num2]:
            q.append((num2,path+"R"))
            visit[num2] = True
        
    