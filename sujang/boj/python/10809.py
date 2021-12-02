data=[-1]*26
for i,s in enumerate(input()):
    if data[ord(s)-ord('a')] == -1:
        data[ord(s)-ord('a')] = i
print(*data)