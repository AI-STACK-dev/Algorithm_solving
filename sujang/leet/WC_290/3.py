from bisect import bisect
from collections import defaultdict


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort()
        repo = defaultdict(list)
        for x,y in rectangles:
            repo[y].append(x)

        ans = []
        for x,y in points:
            temp = 0
            for z in range(y,101):
                temp += len(repo[z]) - bisect.bisect_left(repo[z], x)
            ans.append(temp)
        return ans
        