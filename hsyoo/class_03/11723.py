import sys

n = int(input())
S = set([])
length = 0
# input = sys.stdin.readline
for _ in range(n):
    command = sys.stdin.readline().strip().split()
    num = None
    if len(command) != 1:
        cmd, num = command[0], command[1]
        num = int(num)

        if cmd == 'add':
            S.add(num)
            length +=1
        elif cmd == 'remove':
            if num in S:
                S.remove(num)
                length -=1
        elif cmd == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            if num in S:
                S.remove(num)
                length -=1
            else:
                S.add(num)
                length +=1
    else:
        cmd = command[0]
        if cmd == 'all':
            if length != 20:
                S = set(list(range(1, 21)))
                length = 20
        else:
            S.clear()
            length = 0
    