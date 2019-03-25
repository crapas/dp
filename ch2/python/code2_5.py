# 2차원 배열 형태의 요금표
cost = [[0] * 4 for i in range(0, 4)]
cost[0] = [0, 10, 75, 94]
cost[1] = [-1, 0, 35, 50]
cost[2] = [-1, -1, 0, 80]
cost[3] = [-1, -1, -1, 0]

# 메모로 사용할 캐시
memo = [[0] * 4 for i in range(0, 4)]

# 출발역(s)에서 도착역(d)까지의 최소 요금을 계산합니다.
def minCost(s, d):  
  if (s == d) or (s == d - 1):
    return cost[s][d]

  # 값이 계산되지 않은 경우에만 블록 안으로 들어가서 계산합니다.
  if memo[s][d] == 0:
    # 재귀 호출을 사용하는 코드와 비슷합니다.
    minValue = cost[s][d]

    for i in range(s + 1, d):
      temp = minCost(s, i) + minCost(i, d)
      if temp < minValue:
        minValue = temp
    
    # 계산된 최소 요금을 캐시에 저장
    memo[s][d] = minValue
  
  return memo[s][d]

s = 0
d = 3
print('%d번 역에서 %d번 역 까지의 최소 비용은 %d입니다.' % (s, d, minCost(s, d)))
