def sum(n):
  # 첫 번째 종료 조건
  if n <= 0:
    return 0
  # 두 번째 종료 조건
  if n == 1:
    return 1
  
  return n + sum(n - 1)

n = int(input('숫자를 하나 입력하세요 : '))
print('1에서 %d까지의 합 : %d' % (n, sum(n)))
  