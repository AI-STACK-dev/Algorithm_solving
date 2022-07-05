import sys; input = sys.stdin.readline;
while True:
    data = list(map(int, input().split()))
    if not data[0] and not data[1] and not data[2]:
        break
    if data[2] - data[1] == data[1] - data[0]:
        print("AP", 2 * data[2] - data[1])
    else:
        print("GP", data[2] ** 2 // data[1])