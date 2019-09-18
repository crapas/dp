def waysToScore(n):
  if n < 0:
    return 0
  if n == 0:
    return 1
  return waysToScore(n - 10) \
         + waysToScore(n - 5) \
         + waysToScore(n - 3)

N = int(input('목적 점수를 입력하세요 : '))
print('%d점까지의 경우의 수는 %d입니다.' % (N, waysToScore(N)))