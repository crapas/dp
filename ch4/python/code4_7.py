def waysToScore(n):
  # 파이썬 리스트는 아래와 같이 일괄 초기화가 가능합니다.
  arr = [0] * (n + 1)

  arr[0] = 1  # 0점까지의 경우의 수는 아무것도 하지 않는 1가지입니다.

  for i in range(1, n + 1):
    if i - 3 >= 0:
      arr[i] += arr[i - 3]
    if i - 5 >= 0:
      arr[i] += arr[i - 5]
    if i - 10 >= 0:
      arr[i] += arr[i - 10]
  return arr[n]    

N = int(input('목적 점수를 입력하세요 : '))
print('%d점 까지의 경우의 수는 %d 입니다.' % (N, waysToScore(N)))