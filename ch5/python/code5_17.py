ENOUGH_MIN = -99999999

def getMax(a, b):
  return a if a > b else b

# value[i]는 길이 i인 철근의 가격입니다.
def maxValue(value, N):
  # maxValues[i] : 길이 i인 철근을 팔 때의 최대 이익
  maxValues = [ENOUGH_MIN] * (N + 1)

  maxValues[0] = 0  # 길이 0인 철근의 가격은 0

  # 길이 1에서 N까지 계산해 올라갑니다.
  for i in range(1, N + 1):
    # 길이 i인 철근은 i 길이에 해당되는 가격표(value[i])까지만 필요합니다.
    for j in range(1, i + 1):
      # i - j 길이의 최대 이익에 j 길이의 철근의 가격을 더하면 i 길이 철근의
      # 판매가격을 구할 수 있으며, 모든 j에 대해서 최대값을 취하면
      # 길이 i인 철근을 판매할 때의 최대 이익을 구할 수 있습니다.
      maxValues[i] = getMax(maxValues[i], \
                            value[j] + maxValues[i - j])
  
  # 완성된 배열을 출력해 봅니다.
  for i in range(0, N + 1):
    print('%3d' % maxValues[i], end = '')
  print()

  return maxValues[N]

value = [0, 1, 5, 8, 9, 10, 17, 17, 20]
N = 8
print('길이 %d인 철근을 잘라서 팔 때 최대 %d의 이익을 얻을 수 있습니다.' % \
       (N, maxValue(value, N)))
  