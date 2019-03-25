def numOfPaths(m, n):
  if (m == 0) and (n == 0):   # 방 (0, 0)
    return 0
  if (m == 0) or (n == 0):    # 첫번째 행 또는 첫번째 열
    return 1
  
  # 재귀 호출
  return numOfPaths(m - 1, n) + numOfPaths(m, n - 1)

M, N = input('방의 구조를 입력하세요 : ').split()
M = int(M)
N = int(N)
print('총 경로의 수는 %d개 입니다.' % numOfPaths(M - 1, N - 1))
