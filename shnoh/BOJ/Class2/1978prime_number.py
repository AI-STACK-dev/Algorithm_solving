import sys
n = int(sys.stdin.readline())
data = [int(x) for x in sys.stdin.readline().split()]
not_prime = set([1])
for i in range(2,35):
    k= 2
    res = 0
    while res < 1000:
        res = k*i
        not_prime.add(res)
        k+=1

cnt = 0
for num in data:
    if num not in not_prime:
        cnt+=1
print(cnt)