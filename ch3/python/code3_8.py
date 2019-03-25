def combination(n, m):
  if (n == 0) or (m == 0) or (n == m):
    return 1
  else:
    return combination(n - 1, m) + combination(n - 1, m - 1)

n, m = input('두 수 n, m을 입력하세요. (n >= m) : ').split()
n = int(n)
m = int(m)
print('C(%d, %d) = %d' %(n, m, combination(n, m)))
