import time
from random import *

num_of_station = int(input('역의 수를 입력하세요 :'))
# 2차원 배열 형태의 요금표
cost = [[0] * num_of_station for i in range(0, num_of_station)]

# 임의의 값으로 요금표를 생성합니다.
for i in range(0, num_of_station):
  for j in range(0, num_of_station):
    if i > j:
      cost[i][j] = -1
    elif i == j:
      cost[i][j] = 0
    else:
      cost[i][j] = randint(1, 10)

# 생성한 요금표를 출력해 봅니다.
for i in range(0, num_of_station):
  print(cost[i])

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

d = num_of_station - 1
start_time = int(round(time.time() * 1000))
print('0번 역에서 %d번 역 까지의 최소 비용은 %d입니다.' % (d, minCost(d)))
end_time = int(round(time.time() * 1000))
print('minCost 함수의 실행 시간 : %d(ms)' % (end_time - start_time))