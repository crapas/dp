import time
N_MAX = 301
M_MAX = 301

result = [[0] * M_MAX for i in range(0, N_MAX)]

def combination(n, m):
  for i in range (0, n + 1):
    for j in range(0, i + 1):
      if j == 0:
        result[i][j] = 1
      elif i == j:
        result[i][j] = 1
      else:
        result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
      if(i == n and j == m):
        return result[i][j]

n, m = input('두 수 n, m을 입력하세요. (n >= m) : ').split()
n = int(n)
m = int(m)
start_time = int(round(time.time() * 1000))
print('C(%d, %d) = %d' %(n, m, combination(n, m)))
end_time = int(round(time.time() * 1000))
print('combination 함수의 실행 시간 : %d(ms)' % (end_time - start_time))