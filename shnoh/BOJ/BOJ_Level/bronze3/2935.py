import sys; input = sys.stdin.readline;
a = int(input())
operator = input().rstrip()
b = int(input())
if operator == '+':
    print(a + b)
else:
    print(a * b)