# class stack:
#     def __init__(self):
#         self.items = []
#     def pop(self):
#         if len(self.items) == 0:
#             print(-1)
#         else:
#             print(self.items.pop())
#     def push(self,value):
#         self.items.append(value)
#     def top(self):
#         if len(self.items) == 0:
#             print(-1)
#         else:
#             print(self.items[-1])
#     def __len__(self):
#         return len(self.items)
#     def empty(self):
#         if len(self.items) == 0:
#             print(1)
#         else:
#             print(0)
import sys;input=sys.stdin.readline
n = int(input().rstrip())
s = []
for _ in range(n):
    cmd = list(input().rstrip().split())
    if cmd[0] == "push":
        s.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if s:
            print(s.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(s))
    elif cmd[0] == "top":
        if s:
            print(s[-1])
        else:
            print(-1)
    else:
        if s:
            print(0)
        else:
            print(1)

