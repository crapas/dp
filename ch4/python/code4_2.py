M = 3
N = 4

def getMin(a, b):
  return a if a < b else b

def minPathCost(cost, m, n):
  if (m == 0) and (n == 0): # 셀 (0, 0)이 목적지인 경우
    return cost[0][0]
  if m == 0:                # 목적지가 제일 윗 행에 있을 때
    return minPathCost(cost, 0, n - 1) + cost[0][n]
  if n == 0:                # 목적지가 제일 왼쪽 열에 있을 때
    return minPathCost(cost, m - 1, 0) + cost[m][0]

  x = minPathCost(cost, m - 1, n)
  y = minPathCost(cost, m, n - 1)
  # gitMin()은 두 수 중 작은 수를 반환하는 도우미 함수입니다.
  return getMin(x, y) + cost[m][n]

cost = [[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]
print('최소 이동 비용은 %d입니다.' % minPathCost(cost, M - 1, N - 1))