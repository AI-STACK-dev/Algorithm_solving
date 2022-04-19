from collections import defaultdict
import sys; input=sys.stdin.readline

data = defaultdict(list)
n = int(input())
for _ in range(n):
    a,b,c = input().rstrip().split()
    data[a].append(b)
    data[a].append(c)

def preOrder(root):
    print(root, end='')
    if data[root][0] != ".":
        preOrder(data[root][0])
    if data[root][1] != ".":
        preOrder(data[root][1])

def inOrder(root):
    if data[root][0] != ".":
        inOrder(data[root][0])
    print(root, end='')
    if data[root][1] != ".":
        inOrder(data[root][1])

def postOrder(root):
    if data[root][0] != ".":
        postOrder(data[root][0])
    if data[root][1] != ".":
        postOrder(data[root][1])
    print(root, end='')

preOrder("A")
print()
inOrder("A")
print()
postOrder("A")
print()
