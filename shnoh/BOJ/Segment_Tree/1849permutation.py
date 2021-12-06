import sys
import math
N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(N)]
tree = [0] * (2 ** (1 + int(math.ceil((math.log2(N))))))
original = [0] * N

def init(start, end, index):
    if start == end:
        tree[index] = 1
        return tree[index]
    mid = ( start + end ) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index *2 + 1)
    return tree[index]

def update(start, end, index, value):
    tree[index] -= 1
    if start == end:
        return end
    mid = (start + end) // 2
    left_val = tree[index * 2]
    if left_val >= value:
        return update(start, mid, index * 2, value)
    else:
        return update(mid + 1, end, index * 2 + 1, value - left_val)
    
init(0, N - 1, 1)
for i in range(N):
    where = update(0, N - 1, 1, data[i] + 1)
    original[where] = i + 1

for num in original:
    print(num)