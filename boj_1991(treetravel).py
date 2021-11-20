import sys
input = sys.stdin.readline

n = int(input())
tree = [''] * (n*n)
tree[0] = 'A'
dic = dict()
dic['A'] = 0
for _ in range(n):
    root, left, right = input().split()
    idx = dic[root]
    tree[idx*2 + 1] = left
    dic[left] = idx*2+1
    tree[idx*2 + 2] = right
    dic[right] = idx*2+2

def preorder(index):
    if tree[index] == '.':
        return ''
    return tree[index] + preorder(index*2+1) + preorder(index*2+2)


def inorder(index):
    if tree[index] == '.':
        return ''
    return inorder(index*2+1) + tree[index] + inorder(index*2+2)


def postorder(index):
    if tree[index] == '.':
        return ''
    return postorder(index*2+1) + postorder(index*2+2) + tree[index]


print(preorder(0))
print(inorder(0))
print(postorder(0))
