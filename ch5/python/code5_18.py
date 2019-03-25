def knapSack(C, weight, value, n):
  # 종료 조건 : 남은 물건이 없거나 배낭이 가득 찼을 때
  if (n <= 0) or (C <= 0):
    return 0

  # n번째 물건의 무게가 C보다 크면 그 물건은 넣을 수 없습니다.
  # 하지만 남은 물건 중에 C보다 작은 다른 물건이 있을지도 모릅니다.
  if weight[n - 1] > C:
    return knapSack(C, weight, value, n - 1)

  # n번째 물건을 배낭에 넣는 경우
  carry = value[n - 1] + \
          knapSack(C - weight[n - 1], weight, value, n - 1)
  
  # n번째 물건을 놔두는 경우
  leave = knapSack(C, weight, value, n - 1)

  return carry if carry > leave else leave

weight = [2, 3, 4, 5]
value = [3, 4, 5, 6]
print('도둑이 가지고 갈 수 있는 가치의 최대값은 %d입니다.' % \
      knapSack(5, weight, value, 4))
