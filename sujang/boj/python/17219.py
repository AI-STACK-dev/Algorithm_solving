import sys; input = sys.stdin.readline
n,m = map(int,input().rstrip().split())

dict = {}
for _ in range(n):
    a,b = input().rstrip().split()
    dict[a] = b

for _ in range(m):
    a = input().rstrip()
    print(dict[a])
    