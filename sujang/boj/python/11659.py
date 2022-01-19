import sys; input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
data = list(map(int,input().rstrip().split()))

prefixSum = 0
sumData = [0]*(n+1)
for i in range(n):
    sumData[i+1] = data[i] + prefixSum
    prefixSum = sumData[i+1]

for _ in range(m):
    a,b = map(int,input().rstrip().split())
    print(sumData[b] - sumData[a-1])
