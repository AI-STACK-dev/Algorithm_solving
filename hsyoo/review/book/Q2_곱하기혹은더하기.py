from collections import deque

s = list(map(int, list(input())))
q = deque(s)
sum_ = 0

while q:
    cur = q.popleft()
    if sum_ <=1 or cur <= 1:
        sum_ += cur
    else:
        sum_ *= cur
print(sum_)