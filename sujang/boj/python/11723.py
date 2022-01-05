import sys; input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    cmd = input().rstrip().split()

    if len(cmd) == 1:
        if cmd[0] == "all":
            s = set(list(range(21)))
        else:
            s = set()

    else:
        if cmd[0] == "add":
            s.add(int(cmd[1]))
        elif cmd[0] == "check":
            print(1 if int(cmd[1]) in s else 0)
        elif cmd[0] == "remove":
            s.discard(int(cmd[1]))
        else:
            if int(cmd[1]) in s:
                s.discard(int(cmd[1]))
            else:
                s.add(int(cmd[1]))
    