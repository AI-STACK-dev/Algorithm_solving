n = int(input())
cmds = list(input().split())

start_coord = [1,1]
for cmd in cmds:
    if cmd == 'L' or cmd == 'R':
        if cmd == 'L' and start_coord[1] == 1:
            continue
        elif cmd == 'L':
            start_coord[1] -= 1
        elif cmd == 'R' and start_coord[1] == n:
            continue
        else:
            start_coord[1] += 1
    else:
        if cmd == 'U' and start_coord[0] == 1:
            continue
        elif cmd == 'U':
            start_coord[0] -= 1
        elif cmd == 'D' and start_coord[0] == n:
            continue
        else:
            start_coord[0] += 1
print(start_coord[0], start_coord[1])
        