def fibonacci(n):
  a = 1
  b = 1
  if (n == 1) or (n == 2):
    return 1

  for cnt in range(3, n + 1):
    c = a + b
    a = b
    b = c

  return c

n = int(input('숫자를 입력하세요 : '))
print('피보나치 수열의 %d번째 항은 %d입니다.' % (n, fibonacci(n)))