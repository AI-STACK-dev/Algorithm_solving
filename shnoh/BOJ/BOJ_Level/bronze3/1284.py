import sys; input = sys.stdin.readline;
while True:
    data = input().rstrip()
    cnt = 1
    if data == '0': break
    for num in data:
        if num == '1':
            cnt += 3
        elif num == '0':
            cnt += 5
        else:
            cnt += 4
    print(cnt)