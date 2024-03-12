class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_child_sum(node):
    if node is None:
        return
    
    add_child_sum(node.left)
    add_child_sum(node.right)

    final_sum = node.data

    if node.left is not None:
        final_sum += node.left.data

    if node.right is not None:
        final_sum += node.right.data

    node.data = final_sum

def insert(node, lvalue, rvalue):
    if lvalue != None:
        node.left = Node(lvalue)
    if rvalue != None:
        node.right = Node(rvalue)

def in_order(node):
    if node == None:
        return
    in_order(node.left)
    print('%d ' % node.data, end = '')
    in_order(node.right)


root = Node(2)
insert(root, 4, 1)
insert(root.left, 6, 9)
insert(root.right, None, 2)
insert(root.left.right, 3, None)

print('만들어진 트리를 중위 순회 탐색으로 출력 : ', end='')
in_order(root)
print()

add_child_sum(root)

print('하위 노드의 합으로 갱신된 트리를 중위 순회 탐색으로 출력 : ', end='')
in_order(root)
print()
