import sys; input = sys.stdin.readline

data = [0]*10001
for _ in range(int(input())):
    num = int(input())
    data[num] += 1
for num in range(1,10001):
    amt = data[num]
    for _ in range(amt):
        print(num)