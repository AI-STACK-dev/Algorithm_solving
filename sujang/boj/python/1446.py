from sys import stdin

n,d = map(int,stdin.readline().rstrip().split())
short = [list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]
distance = [i for i in range(d+1)]

for i in range(d+1):
    if i != 0:
        distance[i] = min(distance[i],distance[i-1]+1)
    for a,b,c in short:
        if i ==a and b <=d and distance[b] > distance[i]+c:
            distance[b] = distance[i]+c
print(distance[-1])