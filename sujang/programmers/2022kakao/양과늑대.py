'''
문제 6.
- 이게 되네
- 15분소요
'''

from copy import deepcopy as dp
maxCount = 0
def solution(info, edges):
    data = [[] for _ in range(len(info))]
    for a,b in edges:
        data[a].append(b)
    
    def dfs(wc,sc,touchable):
        global maxCount
        if sc > maxCount:
            maxCount = sc
            
        for node in touchable:
            if info[node] == 1 and sc > wc + 1:
                temp = dp(touchable)
                temp.remove(node)
                temp.extend(data[node])
                dfs(wc+1, sc, temp)
            if info[node] == 0:
                temp = dp(touchable)
                temp.remove(node)
                temp.extend(data[node])
                dfs(wc, sc+1, temp)
        return
                
    dfs(0,1,dp(data[0]))
    print(maxCount)


a = [0,0,1,1,1,0,1,0,1,0,1,1]
b = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
solution(a,b)