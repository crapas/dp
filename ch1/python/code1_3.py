def sum(n):
  return 0 if n <= 0 else (1 if n == 1 else n + sum(n - 1))

n = int(input('숫자를 하나 입력하세요 : '))
print('1에서 %d 까지의 합 : %d' % (n, sum(n)))
  