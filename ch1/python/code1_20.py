def factorial(n):
  f = 1
  for i in range(2, n + 1):
    f = f * i
  return f

n = int(input('숫자를 입력하세요 : '))
print('%d! = %d입니다.' % (n, factorial(n)))
