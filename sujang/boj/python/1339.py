import sys; input = sys.stdin.readline

n = int(input().rstrip())
ch = {}
strings = []
for i in range(n):
    string = input().rstrip()
    strings.append(string)
    length = len(string)
    for j in range(length):
        if not string[j] in ch.keys():
            ch[string[j]] = 10**(length - j-1)
        else:
            ch[string[j]] += 10**(length - j - 1)

ch = sorted(ch.items(), key =lambda x:x[1], reverse=True)
new_ch = {}
first = 9
for i in ch:
    new_ch[i[0]] = first
    first -= 1

ans = 0
for string in strings:
    length = len(string)
    for j in range(length):
        ans += new_ch[string[j]]*(10**(length - j - 1))
print(ans)        