word = list(str(input()))
cnt = {'0' : 0, '1' : 0}
pre = word[0]
for idx, case in enumerate(word[1:]):
    if pre != case:
        cnt[pre] += 1
        pre = case
    elif idx == len(word)-2:
        cnt[pre] +=1
    else:
        continue
print(cnt)
print(min(cnt.values()))