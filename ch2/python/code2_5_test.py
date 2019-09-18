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

# 생성한 요금표를 출력해봅니다.
for i in range(0, num_of_station):
  print(cost[i])

# 메모로 사용할 캐시
memo = [[0] * num_of_station for i in range(0, num_of_station)]

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
d = num_of_station - 1
start_time = int(round(time.time() * 1000))
print('%d번 역에서 %d번 역까지의 최소 비용은 %d입니다.' % (s, d, minCost(s, d)))
end_time = int(round(time.time() * 1000))
print('minCost 함수의 실행 시간 : %d(ms)' % (end_time - start_time))