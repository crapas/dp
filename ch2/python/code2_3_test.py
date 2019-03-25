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
def minCost(s, d):
  if (s == d) or (s == d - 1):
    return cost[s][d]
  minValue = cost[s][d]
  # 최소값을 찾기 위해서 모든 중간 역에 대해서 계산해 봅니다.
  for i in range(s + 1, d):
    # s번 역에서 i번 역까지의 최소 요금과
    # i번 역에서 d번 역까지의 최소 요금의 합
    temp = minCost(s, i) + minCost(i, d)
    if temp < minValue:
      minValue = temp
  
  return minValue

s = 0
d = num_of_station - 1
start_time = int(round(time.time() * 1000))
print('%d번 역에서 %d번 역 까지의 최소 비용은 %d입니다.' % (s, d, minCost(s, d)))
end_time = int(round(time.time() * 1000))
print('minCost 함수의 실행 시간 : %d(ms)' % (end_time - start_time))