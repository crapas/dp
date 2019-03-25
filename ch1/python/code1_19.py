def factorial(n):
  if (n == 1) or (n == 0):
    return 1
  else:
    return n * factorial(n - 1)

n = int(input('숫자를 입력하세요 : '))
print('%d! = %d입니다.' % (n, factorial(n)))
