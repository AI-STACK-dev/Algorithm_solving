def spliter(string):
    s = string.lstrip("{").rstrip("}").split("},{")
    temp = []
    for i in s:
        temp.append(list(map(int,i.split(","))))
    return temp 
    
def solution(s):
    l = spliter(s)
    l.sort(key = lambda x : len(x))
    
    ans = []
    prev = set()
    for i in l:
        if len(i) == 1:
            ans.append(i[0])
            prev.add(i[0])
        else:
            i = set(i)
            intersection = i & prev
            result = (i - intersection).pop()
            ans.append(result)
            prev.add(result)
    return ans
