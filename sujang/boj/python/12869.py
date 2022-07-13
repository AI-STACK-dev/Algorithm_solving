from itertools import permutations
import sys; input = sys.stdin.readline
from collections import deque

n = int(input())
data = list(map(int, input().split())) + (3-n)*[0]
data.sort()
visited = [[[False]*61 for _ in range(61)] for _ in range(61)]
attacks = list(permutations([9,3,1],3))

def bfs():
    q = deque([[*data,0]])
    while q:
        curr = q.popleft()
        
        if curr[2] == 0:
            return curr[3]
        
        for case in attacks:
            next_ = [0]*3
            for i in range(3):
                next_[i] = curr[i] - case[i] if curr[i] - case[i] > 0 else 0
        
            next_.sort()

            if not visited[next_[0]][next_[1]][next_[2]]:
                visited[next_[0]][next_[1]][next_[2]] = True
                q.append([*next_, curr[3]+1])

print(bfs())
