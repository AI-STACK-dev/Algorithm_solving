import sys; input = sys.stdin.readline;
n = int(input())
data = [2,3,4,5,6,7,2]
Sum = 0
for i in range(7):
    Sum += data[i] * (n % 10)
    n = n // 10
res = Sum % 11
if res == 0:
    print("J")
elif res == 10:
    print("Z")
else:
    print(chr(res + 64))