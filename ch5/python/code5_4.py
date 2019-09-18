# 주의 : 재귀 호출 버전(code5_3.c)의 numOfPaths() 함수와
# 매개변수가 다릅니다. 
# - 재귀 호출 버전의 numPaths(3, 2)는 4x3개의 방의 경로 계산
# - 이 버전의 numPaths(3, 2)는 3x2개의 방의 경로 계산
def numOfPaths(m, n):
  cache = [[0] * n for i in range(0, m)]

  for i in range(1, m):
    cache[i][0] = 1
  
  for j in range(1, n):
    cache[0][j] = 1

  for i in range(1, m):
    for j in range(1, n):
      cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
  
  return cache[m - 1][n - 1]

M, N = input('방의 구조를 입력하세요 : ').split()
M = int(M)
N = int(N)
print('총 경로의 수는 %d개입니다.' % numOfPaths(M, N))
