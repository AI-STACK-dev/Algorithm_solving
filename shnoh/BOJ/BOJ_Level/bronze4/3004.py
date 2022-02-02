import sys; input = sys.stdin.readline;
data = int(input())
a = data // 2 + 1
if data % 2 == 1:
    print(a * (a + 1))
else:
    print(a ** 2)