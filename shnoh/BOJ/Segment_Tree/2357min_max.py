import sys
import math
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(N)]
min_tree = [0] * (2 ** (1 + int(math.ceil((math.log2(N))))))
max_tree = [0] * (2 ** (1 + int(math.ceil((math.log2(N))))))

def initMin(start, end, index): # tree 만들기
    if start == end:
        min_tree[index] = data[start]
        return min_tree[index]
    mid = ( start + end ) // 2
    min_tree[index] = min(initMin(start, mid, index * 2), initMin(mid + 1, end, index *2 + 1))
    return min_tree[index]

def initMax(start, end, index): # tree 만들기
    if start == end:
        max_tree[index] = data[start]
        return max_tree[index]
    mid = ( start + end ) // 2
    max_tree[index] = max(initMax(start, mid, index * 2), initMax(mid + 1, end, index *2 + 1))
    return max_tree[index]

def queryMin(start, end, index, left, right):
    if left > end or right < start:
        return math.inf
    if left <= start and right >= end:
        return min_tree[index]
    mid = (start + end) // 2
    return min(queryMin(start, mid, index * 2, left, right), queryMin(mid + 1, end, index * 2 + 1,left, right))

def queryMax(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return max_tree[index]
    mid = (start + end) // 2
    return max(queryMax(start, mid, index * 2, left, right), queryMax(mid + 1, end, index * 2 + 1,left, right))

initMin(0, N - 1, 1)
initMax(0, N - 1, 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(queryMin(0, N - 1, 1, a - 1, b - 1), queryMax(0, N - 1, 1, a - 1, b - 1))