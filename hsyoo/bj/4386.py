import sys
import math

input = sys.stdin.readline
n = int(input())
coords = []
parent = [0] * n
for _ in range(n):
    x,y = map(float, input().split())
    coords.append((x,y))
edges = []
for i in range(n-1):
    for j in range(i+1, n):
        a = coords[i]
        b = coords[j]
        cost = math.sqrt((a[0]-b[0])**2 + (a[1] - b[1])**2)
        edges.append((cost, i,j))

for i in range(n):
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
# print(edges)

edges.sort()
result = 0 
for edge in edges:
    cost, a,b = edge
    # print(a,b)
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a,b)
print(round(result, 2))

