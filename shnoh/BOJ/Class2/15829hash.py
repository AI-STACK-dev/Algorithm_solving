import sys; input = sys.stdin.readline;
L = int(input())
s = input().rstrip()
M = 1234567891
r = 31
H = 0
for i in range(L):
    H += (ord(s[i]) - 96) * r ** i
H = H % M
print(H)