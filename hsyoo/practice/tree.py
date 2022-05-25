class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

root = Node(10)
root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)

print(preorder(root))
print(inorder(root))
print(postorder(root))

