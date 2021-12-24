import sys; input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    num = int(input().rstrip())
    if stack and num ==0:
        stack.pop()
    elif num != 0:
        stack.append(num)
print(sum(stack))
