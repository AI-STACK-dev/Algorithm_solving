import sys; input = sys.stdin.readline;

data = input().rstrip()
# 최소가 되려면? +도 앞의 -로 묶으면 된다.
check = False
res = 0
num = ""
pm = "+"
for c in data:
    if c == '-':
        if pm == '+' and not check:
            res += int(num)
        else:
            res -= int(num)
        num = ""
        check = True
        pm = '-'
    elif c == '+':
        if pm == '+' and not check:
            res += int(num)
        else:
            res -= int(num)
        num = ""
        if check:
            pm = '-'
        else:
            pm = '+'
    else: # 숫자
        num += c # 문자
if pm == '+' and not check:
    res += int(num)
else:
    res -= int(num)
print(res)
