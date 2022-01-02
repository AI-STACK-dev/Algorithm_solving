import sys; input = sys.stdin.readline;
N = int(input())
# 101 103. 103까지의 소수를 구하면 될듯.
sieve = [True] * 104
for i in range(2, 104):
    if sieve[i] == True:
        for j in range(2 * i, 104, i):
            sieve[j] = False
prime = [i for i in range(2, 104) if sieve[i] == True]
n = len(prime)
for i in range(n - 1):
    k = prime[i] * prime[i + 1]
    if k > N:
        print(k)
        break
