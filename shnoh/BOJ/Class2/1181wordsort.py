import sys
n = int(sys.stdin.readline())
A = []
for _ in range(n):
    A.append(sys.stdin.readline().rstrip())
data = list(set(A))
data.sort() # 알페벳 순서로 정렬
data.sort(key=len) # 길이 순서로 정렬
# 이를 통해 python의 sort는 stable 함을 알 수 있다. ex) merge sort
for word in data:
    print(word)
