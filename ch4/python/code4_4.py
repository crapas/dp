M = 3
N = 4

def getMin(a, b):
  return a if a < b else b

def minPathCost(cost, m, n):
  MEM = [[0] * N for i in range(0, M)]
  MEM[0][0] = cost[0][0]

  # 제일 윗쪽 행
  for j in range(0, N):
    MEM[0][j] = MEM[0][j - 1] + cost[0][j]
  
  # 제일 왼쪽 열
  for i in range(0, M):
    MEM[i][0] = MEM[i - 1][0] + cost[i][0]

  # 나머지 셀을 채워 나갑니다.
  for i in range(1, M):
    for j in range(1, N):
      MEM[i][j] = getMin(MEM[i - 1][j], MEM[i][j - 1]) + cost[i][j]

  # 완성된 배열을 출력해 봅시다.
  for i in range(0, M):
    for j in range(0, N):
      print ('%3d' % MEM[i][j], end='')
    print()

  return MEM[M - 1][N - 1]

cost = [[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]
print('최소 이동 비용은 %d입니다.' % minPathCost(cost, M - 1, N - 1))