
# 출발역(0)에서 도착역(N)까지의 최소 요금을 계산합니다.
def min_cost(cost):  
    N = len(cost) - 1
    # minValue[i] = 0번 역에서 i번 역까지의 최소 요금
    min_value = []
    min_value.append(0)
    # cost[j][i] : j번 역에서 i번 역까지 바로 가는 요금
    min_value.append(cost[0][1])

    for i in range(2, N + 1):
        min_value.append(cost[0][i])
        for j in range(1, i):
            min_value[i] = min(min_value[i], min_value[j] + cost[j][i])
    return min_value[N]

cost = [
    [0, 10, 75, 94],
    [-1, 0, 35, 50],
    [-1, -1, 0, 80],
    [-1, -1, -1, 0]
]
d = 3
print('0번 역에서 %d번 역까지의 최소 비용은 %d입니다.' % (d, min_cost(cost)))
