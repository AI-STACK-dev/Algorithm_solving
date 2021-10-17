from sys import stdin

n = int(stdin.readline().rstrip())
a = list(map(int,stdin.readline().rstrip().split()))
add,sub,mul,div = map(int,stdin.readline().rstrip().split())

mini = 1e9
maxi = -1e9

def func(i,now):
    global mini,maxi,add,sub,mul,div
    if i==n:
        mini = min(now,mini)
        maxi = max(now,maxi)
    else:
        if add > 0:
            add -=1
            func(i+1,now+a[i])
            add +=1
        if sub > 0:
            sub -=1
            func(i+1,now-a[i])
            sub +=1
        if mul > 0:
            mul -=1
            func(i+1,now*a[i])
            mul +=1
        if div > 0:
            div -=1
            func(i+1,int(now/a[i]))
            div +=1


func(1,a[0])

print(maxi)
print(mini)