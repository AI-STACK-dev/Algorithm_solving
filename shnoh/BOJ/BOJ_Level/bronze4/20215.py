import sys; input = sys.stdin.readline;
w, h = map(int, input().split())
diagonal = (w ** 2 + h ** 2) ** 0.5
print(abs(diagonal - w - h))