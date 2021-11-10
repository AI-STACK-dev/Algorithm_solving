import sys
n, k = map(int, sys.stdin.readline().split())
factorial = [1] * 11
for i in range(2,11):
    factorial[i] = factorial[i - 1] * i
res = factorial[n] // (factorial[k] * factorial[n-k])
print(res)