def power(x, n):
  if n == 0:
    return 1
  elif x == 1:
    return x
  else:
    return x * power(x, n - 1)

x, n = input('두 수를 입력하세요 : ').split()
x = int(x)
n = int(n)

print('%d ^ %d = %d' % (x, n, power(x, n)))