import sys; input = sys.stdin.readline;
# 결국 5가 몇번 곱해지는 지 세면되겠다. 5. 25. 125. 주의
n = int(input())
cnt = n // 5 + n // 25 + n // 125
print(cnt)