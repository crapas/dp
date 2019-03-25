def sum(n):
  if n == 1:
    return 1
  else:
    return n + sum(n - 1)

n = int(input('숫자를 하나 입력하세요 : '))
print('1에서 %d 까지의 합 : %d' % (n, sum(n)))
