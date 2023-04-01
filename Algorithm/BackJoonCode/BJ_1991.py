#트리 순회/전위 중위 후위
import sys
input = sys.stdin.readline
n = int(input())
nodes = [list(input().split()) for _ in range(n)]
tree = {}
for idx, l, r in nodes:
    tree[idx] = [l, r]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')
