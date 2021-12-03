import sys; input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

cnt = 0
for d in data:
    i = 2
    isPrime = True
    while i*i <= d:
        if d%i == 0:
            isPrime = False     
            break   
        i+=1 
    if isPrime and d >=2:
        cnt +=1
print(cnt)