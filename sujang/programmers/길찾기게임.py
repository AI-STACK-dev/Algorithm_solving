import sys
sys.setrecursionlimit(10**6)

def preOrder(ns, ans):
    n = len(ns)
    root = ns[0]
    left,right = [],[]
    for i in range(1,n):
        if ns[i][0] < root[0]:
            left.append(ns[i])
        else:
            right.append(ns[i])
    ans.append(root[2])
    if left:
        preOrder(left, ans)
    if right:
        preOrder(right,ans)
    
def postOrder(ns, ans):
    n = len(ns)
    root = ns[0]
    left,right = [],[]
    for i in range(1,n):
        if ns[i][0] < root[0]:
            left.append(ns[i])
        else:
            right.append(ns[i])
    if left:
        postOrder(left, ans)
    if right:
        postOrder(right,ans)
    ans.append(root[2])
    
def solution(nodes):
    preAns, postAns = [],[]
    
    n = len(nodes)
    for i in range(n):
        nodes[i].append(i+1)
    sortedNodes = sorted(nodes, key = lambda x : (-x[1], x[0]))
    
    preOrder(sortedNodes, preAns)
    postOrder(sortedNodes, postAns)
    
    return [preAns, postAns]