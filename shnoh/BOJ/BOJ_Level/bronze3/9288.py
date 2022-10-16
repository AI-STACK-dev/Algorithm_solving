import sys; input = sys.stdin.readline;
t = int(input())
for i in range(t):
    print(f'Case {i + 1}:')
    S = int(input())
    half = S // 2
    if S > 7:
        for j in range(S - 6, half + 1):
            print(f'({j},{S - j})')
    else:
        for j in range(1, half + 1):
            print(f'({j},{S - j})')