import sys;input = sys.stdin.readline

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
parent = list(range(n))

x,y,z = [],[],[]
for i in range(n):
    a,b,c = map(int,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

edges.sort()
result = 0
for cost,a,b in edges:
    if find(a) != find(b):
        union(a,b)
        result += cost

print(result) 