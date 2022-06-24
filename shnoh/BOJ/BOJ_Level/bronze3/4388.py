import sys; input = sys.stdin.readline;
while True:
    a, b = input().split()
    if a == b == '0': break
    if len(a) < len(b):
        a = (len(b) - len(a)) * '0' + a
    else:
        b = (len(a) - len(b)) * '0' + b
    res = 0
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        if int(a[i]) + int(b[i]) + carry >= 10:
            carry = 1
            res += 1
        else:
            carry = 0
    print(res)