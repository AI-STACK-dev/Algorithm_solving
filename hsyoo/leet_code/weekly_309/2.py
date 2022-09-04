#양수를 받는다. start position에서 왼쪽 오른쪽 선택 가능.
# 경우의 수를 세는 문제.
# k 스텝만큼 움직여서 endPos까지 도달해야함.
# 서치를 어떻게 해야하지?
# 1에서 2까지 도달할 때, 2갔다가 3갔다가 2다시가기. 
# 첫 번째 생각 end - start 했을 때, k로 -, +를 해서 만들 수 있는 수인가? k가 3인 경우,
# + + - --> end - start == 1
# + - + , - + +
# start:2, end:5, k = 10 k는 짝수인데, +, -를 여러개 조합한다고 차가 3인걸 구할 수 있는가?
# +:7, -: 3 --> diff 4 // +: 6, -: 4 --> diff 2 => 못함.
# 만약 k가 9라면 가능한가?(홀수) -- + 6, -:3 x / + 5 - 4 x 
# 음... True or False는 풀 수 있을 것 같은데, 경우의 수를 어떻게 구하지? 
# bfs인가? 왼쪽 오른쪽. 

# from collections import deque

# dx = [-1, 1]

# class Solution:
#     def numberOfWays(self, startPos, endPos, k):
#         answer = 0
#         q = deque([(startPos, 0)])
#         while q:
#             x, cnt = q.popleft()
#             # print(x, cnt)
#             if x == endPos and cnt == k:
#                 answer += 1
#             if cnt >= k:
#                 continue

#             for i in range(2):
#                 nx = x + dx[i]
#                 q.append((nx, cnt + 1))
#             # print(q)
#         return answer % (int(1e9) + 7)

from functools import lru_cache

class Solution:
    def numberOfWays(self, startPos, endPos, k):
        @lru_cache(maxsize = None)
        def dfs(position, moves):
            if moves == k:
                # print(int(position == endPos))
                if position == endPos:
                    return 1
                else:
                    return 0
                # return int(position == endPos)
            if abs(position - endPos) > k - moves:
                return 0
            return dfs(position+1, moves+1) + dfs(position -1, moves + 1)
        return (dfs(startPos+1,1) + dfs(startPos-1, 1)) % (10**9 + 7)
        
print(Solution().numberOfWays(1,2,3))
print(Solution().numberOfWays(2, 5, 10))