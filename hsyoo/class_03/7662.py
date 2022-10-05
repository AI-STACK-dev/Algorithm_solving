# import sys
# import heapq

# input = sys.stdin.readline
# T = int(input().rstrip())
# for _ in range(T):
#     q = []
#     k = int(input().rstrip())
#     for _ in range(k):
#         cmd, num = input().rstrip().split()
#         num = int(num)
        
#         if len(q) == 0 and cmd == 'D':
#             continue
#         if cmd == 'I':
#             heapq.heappush(q, num)
#         elif cmd == 'D' and  num == 1:
#             q.remove(heapq.nlargest(1, q)[0])
#         elif cmd == 'D' and num == -1:
#             heapq.heappop(q)
#     if len(q) == 0:
#         print("EMPTY")
#     else:
#         print(heapq.nlargest(1, q)[0], heapq.heappop(q))
    

import sys;read=sys.stdin.readline
import heapq

result=[]
for T in range(int(read())):
    visited=[False]*1_000_001
    minH,maxH=[],[]
    for i in range(int(read())):
        s=read().split()
        if s[0]=='I':
            heapq.heappush(minH,(int(s[1]),i))
            heapq.heappush(maxH,(-int(s[1]),i))
            visited[i]=True
        elif s[1]=='1':
            while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
            if maxH:
                visited[maxH[0][1]]=False
                heapq.heappop(maxH)
        else:
            while minH and not visited[minH[0][1]]:heapq.heappop(minH)
            if minH:
                visited[minH[0][1]]=False
                heapq.heappop(minH)
    while minH and not visited[minH[0][1]]:heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
    result.append(f'{-maxH[0][0]} {minH[0][0]}'if maxH and minH else'EMPTY')
print('\n'.join(result))