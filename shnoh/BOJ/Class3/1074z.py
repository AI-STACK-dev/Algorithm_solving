import sys; input = sys.stdin.readline
# 그냥 이론 배운거 없이 생각으로 구상한게 바로 되네^^ So Happy!
def Z(ret, n, r, c):
    if n == 0:
        return ret
    k = 2 ** (n - 1)
    if r >= k:
        if c >= k:
            return Z(ret + 2 ** (2 * n) * 3 // 4, n - 1, r - k, c - k)
        else:
            return Z(ret + 2 ** (2 * n) // 2, n - 1, r - k, c)
    else:
        if c >= k:
            return Z(ret + 2 ** (2 * n) // 4, n - 1, r, c - k)
        else:
            return Z(ret, n - 1, r, c)

n, r, c = map(int, input().split())
print(Z(0, n, r, c))
