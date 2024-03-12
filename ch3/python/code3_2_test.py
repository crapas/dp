import time
from random import randint


# 출발역(0)에서 도착역(N)까지의 최소 요금을 계산합니다.
def min_cost(cost):  
    N = len(cost) - 1
    # min_value[i] = 0번 역에서 i번 역까지의 최소 요금
    min_value = []
    min_value.append(0)
    # cost[j][i] : j번 역에서 i번 역까지 바로 가는 요금
    min_value.append(cost[0][1])

    for i in range(2, N + 1):
        min_value.append(cost[0][i])
        for j in range(1, i):
            min_value[i] = min(min_value[i], min_value[j] + cost[j][i])
    return min_value[N]



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

d = num_of_station - 1
start_time = int(round(time.time() * 1000))
print('0번 역에서 %d번 역까지의 최소 비용은 %d입니다.' % (d, min_cost(cost)))
end_time = int(round(time.time() * 1000))
print('minCost 함수의 실행 시간 : %d(ms)' % (end_time - start_time))