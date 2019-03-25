class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# 선행 재귀의 경우 먼저 리스트의 나머지를 탐색하고 난 후에
# 현재 노드의 값을 출력합니다.
def traverse1(head):
  if head != None:
    traverse1(head.next)
    print('%d' % head.data, end=' ')

# 후행 재귀의 경우 현재 노드의 값을 출력한 다음
# 리스트의 나머지를 탐색합니다.
def traverse2(head):
  if head != None:
    print('%d' % head.data, end=' ')
    traverse2(head.next)

l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l1.next = l2
l2.next = l3
l3.next = l4

print('traverse1 함수(선행 재귀)의 출력 : ', end = '')
traverse1(l1)
print('\ntraverse2 함수(후행 재귀)의 출력 : ', end = '')
traverse2(l1)
print()