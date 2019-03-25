ENOUGH_MIN = -99999999
# 두 수 중 큰 수를 반환하는 도우미 함수
def getMax(a, b):
  return a if a > b else b

# value[i]는 길이 i인 철근의 가격입니다.
def maxValue(value, N):
  # 종료 조건 : 남은 철근이 없을 때
  if N <= 0:
    return 0

  # 최대 이익
  price = ENOUGH_MIN

  for i in range(1, N + 1):
    price = getMax(price, \
                   value[i] + maxValue(value, N - i))
  
  return price

value = [0, 1, 5, 8, 9, 10, 17, 17, 20]
N = 8
print('길이 %d인 철근을 잘라서 팔 때 최대 %d의 이익을 얻을 수 있습니다.' % \
       (N, maxValue(value, N)))
  