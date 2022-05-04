def solution(n, k, cmd):
    ans = ["O"]*n
    stack = []
    # define linked list
    linkedList = {}
    for i in range(n):
        linkedList[i] = [i-1,i+1]
    linkedList[0] = [None, 1]
    linkedList[n-1] = [n-2,None]
    # cmd
    for c in cmd:
        cs = c.split()
        # delete
        if cs[0] == "C":
            ans[k] = "X"
            stack.append(k)
            prev, nex = linkedList[k]
            if prev != None:
                linkedList[prev][1] = nex
            if nex != None:
                linkedList[nex][0] = prev
                k = nex
            else:
                k = prev
        # undo
        elif cs[0] == "Z":
            idx = stack.pop()
            ans[idx] = "O"
            prev,nex = linkedList[idx]
            if prev != None:
                linkedList[prev][1] = idx
            if nex != None:
                linkedList[nex][0] = idx
        # move
        else:
            amt = int(cs[1])
            if cs[0] == "U":
                param = 0
            else:
                param = 1
            for _ in range(amt):
                k = linkedList[k][param]
    return "".join(ans)