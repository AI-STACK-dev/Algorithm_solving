import sys;input = sys.stdin.readline

n = int(input())
cnt = 0
cmds = []
stack = []

for i in range(n):
    target = int(input())

    while cnt < target:
        cnt += 1
        stack.append(cnt)
        cmds.append('+')
    
    if stack[-1] == target:
        stack.pop()
        cmds.append("-")
    else:
        print("NO")
        exit(0)
print(*cmds,sep='\n')