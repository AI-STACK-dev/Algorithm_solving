import sys; input = sys.stdin.readline;
def factor(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            k = n // i
            if k not in factors:
                factors.append(k)
    factors.sort()
    return factors
p, q = map(int, input().split())
pfac = factor(p)
qfac = factor(q)
for x in pfac:
    for y in qfac:
        print(x, y)