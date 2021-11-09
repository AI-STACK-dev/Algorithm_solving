__import__('sys').setrecursionlimit(123123)

from sys import stdin

def find_parent(parent,a):
    if a != parent[a]:
        parent[a]  = find_parent(parent,parent[a])
    return parent[a]

def union(parent,P,a,b):
    if a == b:
        return 
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
        p[b] += p[a]
    else:
        parent[b] = a
        p[a] += p[b]
# input
n,m = map(int,stdin.readline().rstrip().split())
edge = []
for _ in range(m):
    a,b,cost = map(int,stdin.readline().rstrip().split())
    edge.append((cost,a-1,b-1))

# sort
edge.sort()

# query
q = int(stdin.readline().rstrip())
qs = [list(map(lambda x :x-1,list(map(int,stdin.readline().rstrip().split())))) for _ in range(q)]

# for parametric search
low = [0] * q
high = [m+1] * q
result = [[0,0] for _ in range(q)]

# do parametric search
while True:
    flag = False
    g = [[] for _ in range(m+1)]
    
    for i in range(q):
        if low[i]+1 < high[i]:
            flag = True
            g[(low[i]+high[i])//2].append(i)
    
    if not flag:
        break
    
    p = [1]*n 
    parent = [i for i in range(n)]
    for i in range(m):
        cost,a,b = edge[i]
        if find_parent(parent,a) != find_parent(parent,b):
            union(parent,p,a,b)
        for j in g[i+1]:
            c,d = qs[j]
            if find_parent(parent,c) == find_parent(parent,d):
                high[j] = i+1
                result[j][0] = cost
                result[j][1] = p[find_parent(parent,c)]
            else:
                low[j] = i+1

for i in range(q):
    if low[i] == m:
        print('-1')
    else:
        print(result[i][0],result[i][1])