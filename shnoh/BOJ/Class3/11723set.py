import sys; input = sys.stdin.readline;
n = int(input())
S = set()
for _ in range(n):
    instruction = input().rstrip().split()
    if instruction[0] == 'all':
        S = set([i for i in range(1,21)])
    elif instruction[0] == 'empty':
        S = set()
    else:
        num = int(instruction[1])
        if instruction[0] == 'add':
            S.add(num)
        elif instruction[0] == 'remove':
            if num in S:
                S.remove(num)
        elif instruction[0] == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif instruction[0] == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.add(num)
        else:
            print("error occurred")