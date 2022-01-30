def findParent(parent,x):
    if parent[x] != x:
        parent[x] = findParent(parent,parent[x])
    return parent[x]

def unionParent(parent,a,b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        parent = list(range(len(words)))
        
        # judge
        