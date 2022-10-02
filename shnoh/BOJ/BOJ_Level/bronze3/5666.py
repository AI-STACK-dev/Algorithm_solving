# 입력이 끝날때까지 입력받기.
import sys; input = sys.stdin.readline;
while True:
    try:
        h, p = map(int, input().split())
        res = h / p
        print(format(round(res, 2), ".2f"))
    except:
        break