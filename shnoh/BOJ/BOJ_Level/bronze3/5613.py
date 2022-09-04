import sys; input = sys.stdin.readline;
cnt = 0
cur = int(input())
while True:
    # print("cnt: ", cnt)
    if cnt % 2:
        n = int(input())
        # print("n: ", n)
        if k == '+':
            cur = cur + n
        elif k == '-':
            cur = cur - n
        elif k == '*':
            cur = cur * n
        elif k == '/':
            cur = cur // n 
    else:
        k = input().rstrip()
    #     print("k: ", k)
    # print("cur: ", cur)
    cnt += 1
    if k == '=':
        print(cur)
        break