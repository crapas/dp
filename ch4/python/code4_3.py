M = 3
N = 4

# 결과를 저장(메모)할 전역 변수(캐시)
MEM = [[0] * N for i in range(0, M)]

def getMin(a, b):
  return a if a < b else b

def minPathCost(cost, m, n):
  # 만약 셀 (m, n)의 최소 이동 비용이 이미 계산되어 있다면
  # 다시 계산하지 않습니다.
  if MEM[m][n] != 0:
    return MEM[m][n]
 
  if (m == 0) and (n == 0):
    MEM[m][n] = cost[0][0]
  elif m == 0:                
    MEM[m][n] = minPathCost(cost, 0, n - 1) + cost[0][n]
  elif n == 0:                
    MEM[m][n] = minPathCost(cost, m - 1, 0) + cost[m][0]
  else:
    x = minPathCost(cost, m - 1, n)
    y = minPathCost(cost, m, n - 1)    
    MEM[m][n] = getMin(x, y) + cost[m][n]
  return MEM[m][n]

cost = [[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]
print('최소 이동 비용은 %d입니다.' % minPathCost(cost, M - 1, N - 1))