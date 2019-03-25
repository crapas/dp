ENOUGH_MIN = -99999999
MAX_N = 10

# 메모를 저장할 배열
maxValues = [ENOUGH_MIN] * MAX_N

def getMax(a, b):
  return a if a > b else b

# value[i]는 길이 i인 철근의 가격입니다.
def maxValue(value, N):
  if N <= 0:
    return 0

  # 이미 계산된 값이 있으면 그 값을 반환
  if maxValues[N - 1] != ENOUGH_MIN:
    return maxValues[N - 1]

  for i in range(1, N + 1):
    maxValues[N - 1] = getMax(maxValues[N - 1], \
                       value[i] + maxValue(value, N - i))
  
  return maxValues[N - 1]

value = [0, 1, 5, 8, 9, 10, 17, 17, 20]
N = 8
print('길이 %d인 철근을 잘라서 팔 때 최대 %d의 이익을 얻을 수 있습니다.' % \
       (N, maxValue(value, N)))
  