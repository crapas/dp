import time
N_MAX = 301
M_MAX = 301

result = [[0] * M_MAX for i in range(0, N_MAX)]
def combination(n, m):
  if (n == 0) or (m == 0) or (n == m):
    return 1
  elif result[n][m] != 0:
    return result[n][m]
  else:
    result[n][m] = combination(n - 1, m) + combination(n - 1, m - 1)
    return result[n][m]

n, m = input('두 수 n, m을 입력하세요. (n >= m) : ').split()
n = int(n)
m = int(m)
start_time = int(round(time.time() * 1000))
print('C(%d, %d) = %d' %(n, m, combination(n, m)))
end_time = int(round(time.time() * 1000))
print('combination 함수의 실행 시간 : %d(ms)' % (end_time - start_time))