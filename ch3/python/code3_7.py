class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def addChildSum(node):
  if node is None:
    return
  
  addChildSum(node.left)
  addChildSum(node.right)

  finalSum = node.data

  if node.left is not None:
    finalSum += node.left.data

  if node.right is not None:
    finalSum += node.right.data

  node.data = finalSum

def insert(node, lvalue, rvalue):
  if lvalue != None:
    node.left = Node(lvalue)
  if rvalue != None:
    node.right = Node(rvalue)

def inOrder(node):
  if node == None:
    return
  inOrder(node.left)
  print('%d ' % node.data, end = '')
  inOrder(node.right)


root = Node(2)
insert(root, 4, 1)
insert(root.left, 6, 9)
insert(root.right, None, 2)
insert(root.left.right, 3, None)

print('만들어진 트리를 중위 순회 탐색으로 출력 : ', end='')
inOrder(root)
print()

addChildSum(root)

print('하위 노드의 합으로 갱신된 트리를 중위 순회 탐색으로 출력 : ', end='')
inOrder(root)
print()
