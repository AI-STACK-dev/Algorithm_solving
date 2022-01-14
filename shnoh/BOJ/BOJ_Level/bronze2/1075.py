import sys; input = sys.stdin.readline;
N = int(input())
F = int(input())
def solve(N,F):
    N = (N // 100) * 100
    for i in range(0,10):
        if (i + N) % F == 0:
            return '0' + str(i)
    for i in range(10,100):
        if (i + N) % F == 0:
            return i
print(solve(N,F))