# https://leetcode.com/contest/weekly-contest-284/
from collections import defaultdict
from heapq import heappush, heappop

class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        g1 = defaultdict(list)
        g2 = defaultdict(list)
        for a,b,w in edges:
            g1[a].append([b,w])
            g2[b].append([a,w])
        
        def dijks(graph,k):
            hp, temp = [(0, k)], {}
            while hp:
                time, node = heappop(hp)
                if node not in temp:
                    temp[node] = time
                    for v,w in graph[node]:
                        heappush(hp,(time+w,v))
            return [ temp.get(i,float("inf")) for i in range(n)]
        
        arr1 = dijks(g1,src1)
        arr2 = dijks(g1,src2)
        arr3 = dijks(g2, dest)

        ans = float("inf")
        for i in range(n):
            ans = min(ans, arr1[i]+arr2[i]+arr3[i])
        return ans if ans != float("inf") else -1
