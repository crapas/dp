class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def insert(node, lvalue, rvalue):
  if lvalue != None:
    node.left = Node(lvalue)
  if rvalue != None:
    node.right = Node(rvalue)

def inOrder(node):
  if node == None:
    return
  if node.left != None:
    inOrder(node.left)
  print(node.data + ' ', end = '')
  if node.right != None:
    inOrder(node.right)

root = Node('A')
insert(root, 'B', 'C')
insert(root.left, 'E', None)
insert(root.right, 'F', 'G')

print('중위 순회 탐색 결과 : ', end='')
inOrder(root)
print()
