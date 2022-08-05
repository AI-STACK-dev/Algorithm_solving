import sys; input = sys.stdin.readline;
h = int(input())
if h == 0:
    print(1)
elif h == 1:
    print(0)
elif h % 2 == 0:
    res = '8' * (h // 2)
    print(int(res))
else:
    res = '4' + '8' * (h // 2)
    print(int(res))