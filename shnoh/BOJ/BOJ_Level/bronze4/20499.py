import sys; input = sys.stdin.readline;
K, D, A = map(int, input().split('/'))
if D == 0 or K + A < D:
    print("hasu")
else:
    print("gosu")