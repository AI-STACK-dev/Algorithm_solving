import sys; input = sys.stdin.readline;
P, K = map(int, input().split())
# K까지의 수 중에 나누어지는 수가 있으면, bad + 그 수 출력.
def solve(P, K):
    for i in range(2, K):
        if P % i == 0:
            print("BAD", i)
            return
    print("GOOD")
    return
solve(P, K)