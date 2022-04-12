import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((c, a, b))
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

result = []
total = 0
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        total += cost
        result.append(cost)
        union_parent(parent, a, b)
max_ = max(result)
print(total - max_)
