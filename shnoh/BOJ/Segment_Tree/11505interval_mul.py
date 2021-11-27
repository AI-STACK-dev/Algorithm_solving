import sys
sys.setrecursionlimit(10**6)

N, M, K = map(int, sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(N)]
tree = [0] * (2 ** 21) # 131,072 * 2
# tree = [0] * (2 * N)

def init(start, end, index): # tree 만들기
    if start == end:
        tree[index] = data[start]
        return tree[index]
    mid = ( start + end ) // 2
    tree[index] = init(start, mid, index * 2) * init(mid + 1, end, index *2 + 1)
    return tree[index] % 1000000007

def interval_mul(start, end, index, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return interval_mul(start, mid, index * 2, left, right) * interval_mul(mid + 1, end, index * 2 + 1,left, right)

def update(start, end, index, what, value):
    if what < start or what > end:
        return
    if start == end:
        tree[index] = value
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)
    tree[index] = tree[index * 2] * tree[index * 2 + 1] % 1000000007

init(0, N - 1, 1)
#print(tree[0:20])
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        data[b - 1] = c
        update(0, N - 1, 1, b - 1, c)
        #print(tree[0:20])
    else:
        print(interval_mul(0, N - 1, 1, b - 1, c - 1) % 1000000007)