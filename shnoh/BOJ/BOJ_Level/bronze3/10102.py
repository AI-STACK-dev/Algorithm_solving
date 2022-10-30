import sys; input = sys.stdin.readline;
v = int(input())
s = input().rstrip()
A = 0
for i in range(v):
    if s[i] == 'A':
        A += 1
B = v - A
if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print("Tie")