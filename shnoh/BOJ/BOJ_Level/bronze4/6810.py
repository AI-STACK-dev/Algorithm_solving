import sys; input = sys.stdin.readline;
data = "9780921418"
data2 = [input().rstrip() for _ in range(3)]
sum = 0
for i in range(10):
    if i % 2: # 홀수면
        sum += int(data[i]) * 3
    else:
        sum += int(data[i])
for i in range(3):
    if i % 2: # 홀수면
        sum += int(data2[i]) * 3
    else:
        sum += int(data2[i])
print("The 1-3-sum is", sum)