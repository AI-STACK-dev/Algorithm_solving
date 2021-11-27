import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
data = [int(x) for x in sys.stdin.readline().split()]
#tree = [0] * (2 ** 17) # 131,072 * 2
tree = [0] * (2 * N)

def init(start, end, index): # tree 만들기
    if start == end:
        tree[index] = data[start]
        return tree[index]
    mid = ( start + end ) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index *2 + 1)
    return tree[index]

def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1,left, right)

# def update(start, end, index, what, value):
#     if what < start or what > end:
#         return
#     tree[index] +=value
#     if start == end:
#         return
#     mid = (start + end) // 2
#     update(start, mid, index * 2, what, value)
#     update(mid + 1, end, index * 2 + 1, what, value)

init(0, N - 1, 1)
for _ in range(M):
    I, J = map(int, sys.stdin.readline().split())
    print(interval_sum(0, N - 1, 1, I - 1, J - 1))