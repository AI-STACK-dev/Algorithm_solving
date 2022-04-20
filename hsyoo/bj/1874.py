"""n = int(input())
operation = []
ary = []
stack = []
for _ in range(n):
    ary.append(n)
cnt = 0
for i in range(1, n+1):
    if i == ary[cnt]:
        operation.append('+')
        operation.append('-')
        cnt += 1
    else:
        stack.append(i)
        """