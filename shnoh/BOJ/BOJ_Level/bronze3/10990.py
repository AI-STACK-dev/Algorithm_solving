import sys; input = sys.stdin.readline;
n = int(input())
blank = " "
print(blank * (n - 1), '*', sep = '')
pre = n - 2
inner = 1
for _ in range(1, n):
    print(blank * pre, '*', blank * inner, '*', sep = '')
    pre -= 1
    inner += 2