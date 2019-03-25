def countWays(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  return countWays(n - 1) + countWays(n - 2)

n = int(input('공간의 가로 길이를 입력하세요 : '))
print('%dx2 공간에 타일을 놓을 수 있는 경우의 수는 %d입니다.' % (n, countWays(n)))