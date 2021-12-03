import sys;input=sys.stdin.readline
a,b = map(int,input().split())
for i in range(a,b+1):
    isPrime = True
    for j in range(2,int(i**0.5)+1):
        if i%j ==0:
            isPrime = False
            break
    if isPrime and i>=2:
        print(i)