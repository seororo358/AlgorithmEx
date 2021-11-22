import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


class Node():
    def __init__(self, key):
        self.num = key
        self.left = None
        self.right = None


class Binary_tree:
    def __init__(self):
        self.root = Node(0)

    def insert(self, key):
        current = self.root
        if current.num == 0:
            current.num = key
            return current.num
        while True:
            if key < current.num:
                if not current.left:
                    current.left = Node(key)
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = Node(key)
                    break
                current = current.right


def postorder(node):
    if node.left is not None:
        postorder(node.left)
    if node.right is not None:
        postorder(node.right)
    print(node.num)


bitree = Binary_tree()
arr = []
while True:
    try:
        value = int(input())
        arr.append(value)

    except:
        break
for i in arr:
    bitree.insert(i)
postorder(bitree.root)
