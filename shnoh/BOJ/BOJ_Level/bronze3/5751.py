import sys; input = sys.stdin.readline;
while True:
    n = int(input())
    if n == 0:
        break
    data = list(map(int, input().split()))
    john = sum(data)
    print(f'Mary won {n - john} times and John won {john} times')