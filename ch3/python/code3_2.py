# 2차원 배열 형태의 요금표
cost = [[0] * 4 for i in range(0, 4)]
cost[0] = [0, 10, 75, 94]
cost[1] = [-1, 0, 35, 50]
cost[2] = [-1, -1, 0, 80]
cost[3] = [-1, -1, -1, 0]

# 출발역(s)에서 도착역(d)까지의 최소 요금을 계산합니다.
def minCost(N):  
  # minValue[i] = 0번 역에서 i번 역까지의 최소 요금
  minValue = []
  minValue.append(0)
  # cost[j][i] : j번 역에서 i번 역까지 바로 가는 요금
  minValue.append(cost[0][1])

  for i in range(2, N + 1):
    minValue.append(cost[0][i])
    for j in range(1, i):
      if minValue[i] > minValue[j] + cost[j][i]:
        minValue[i] = minValue[j] + cost[j][i]
  return minValue[N]

d = 3
print('0번 역에서 %d번 역 까지의 최소 비용은 %d입니다.' % (d, minCost(d)))
