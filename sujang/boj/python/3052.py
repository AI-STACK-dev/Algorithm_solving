ans = []
for _ in range(10):
    ans.append(int(input())%42)
print(len(set(ans)))