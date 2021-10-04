n = int(input())
cnt = 0
for i in range((n+1)*3600):
    h = str(i//3600)
    m = str((i%3600)//60)
    s = str(i%60)
    
    if '3' in h or '3' in m or '3' in s:
        cnt +=1
        print(h, m, s)
print(cnt)