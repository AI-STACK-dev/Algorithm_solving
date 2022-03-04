import sys; input = sys.stdin.readline
n = int(input())
cnt = 0
for _ in range(n):
    word = input().rstrip()
    d = [word[0]]
    ans = True
    for w in word:
        if w in d and w != d[-1]:
            ans = False
            break
        d.append(w)
    if ans:
        cnt += 1
print(cnt)
