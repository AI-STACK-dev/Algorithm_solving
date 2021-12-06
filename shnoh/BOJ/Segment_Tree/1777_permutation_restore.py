import sys
import math
N = int(sys.stdin.readline())
data = [int(x) for x in sys.stdin.readline().split()]
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
    right_val = tree[index * 2 + 1]
    if right_val >= value:
        return update(mid + 1, end, index * 2 + 1, value)
    else:
        return update(start, mid, index * 2, value - right_val)
    
init(0, N - 1, 1)
for i in range(N - 1, -1, -1):
    where = update(0, N - 1, 1, data[i] + 1)
    original[where] = i + 1

print(*original)