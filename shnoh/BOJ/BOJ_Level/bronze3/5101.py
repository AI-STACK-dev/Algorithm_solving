import sys; input = sys.stdin.readline;
while True:
    first, diff, test = map(int, input().split())
    if diff == 0:
        break
    if (test - first) % diff != 0 or (test - first) * diff < 0:
        print('X')
    else:
        print(1 + (test - first) // diff)