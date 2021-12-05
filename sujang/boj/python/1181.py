import sys;input=sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    d = input().rstrip()
    if not d in data:
        data.append(d)
print(*sorted(data, key=lambda x : (len(x),x)),sep='\n')