import sys
n = int(sys.stdin.readline())
N = [int(i) for i in sys.stdin.readline().split()]
A = set(N)
m = int(sys.stdin.readline())
M = [int(i) for i in sys.stdin.readline().split()]
for num in M:
    if num in A:
        print(1)
    else:
        print(0)
