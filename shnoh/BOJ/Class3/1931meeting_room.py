import sys; input = sys.stdin.readline;
# 강의실, 회의실 배정 문제. 전형적인 그리디
# 빨리 끝나는 것 먼저 배치.
# 가장 먼저 끝나고. 다음 작은 게, 겹치면, 그 다음 적은 걸로. n개 sort 하고 검사하면 되네.
# 시작과 동시에 끝나는 경우 : 3,3과 3,5 와 5,5가 주어졌으면 5,5가 먼저sort되면, 끝이 5이므로 3,5가 성립될 수 없다.
# 따라서 더 시작시간을 second key로 sort
n = int(input())
data = []

for i in range(n):
    a, b = map(int, input().split())
    data.append([a,b])
data.sort(key = lambda x : (x[1],x[0]))
res = 1
last = data[0][1]
for i in range(1, n):
    if last <= data[i][0]:
        last = data[i][1]
        res += 1
print(res)