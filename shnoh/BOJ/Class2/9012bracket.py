import sys
input = sys.stdin.readline

def check(data):
    stack = []
    for bracket in data:
        if bracket == '(':
            stack.append(bracket)
        elif not stack: # 비었으면
            return "NO"
        else:
            stack.pop()
    if stack:
        return "NO"
    else:
        return "YES"

T = int(input())
for _ in range(T):
    data = input().rstrip()
    print(check(data))