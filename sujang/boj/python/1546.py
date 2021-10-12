from sys import stdin

n = int(stdin.readline())
data = list(map(int,stdin.readline().split()))

m = max(data)
s = sum(data)
print((s*100)/(m*n))
