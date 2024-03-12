# 출발역(s)에서 도착역(d)까지의 최소 요금을 계산합니다.
def min_cost(s, d, cost):
    if s == d or s == d - 1:
        return cost[s][d]
    min_value = cost[s][d]
    # 최솟값을 찾기 위해서 모든 중간 역에 대해서 계산해봅니다.
    for i in range(s + 1, d):
        # s번 역에서 i번 역까지의 최소 요금과
        # i번 역에서 d번 역까지의 최소 요금의 합
        cost_s_i_d = min_cost(s, i, cost) + min_cost(i, d, cost)
        min_value = min(min_value, cost_s_i_d)
        
    return min_value

# 2차원 배열 형태의 요금표
cost = [
    [0, 10, 75, 94],
    [-1, 0, 35, 50],
    [-1, -1, 0, 80],
    [-1, -1, -1, 0]
]
s = 0
d = 3
print('%d번 역에서 %d번 역까지의 최소 비용은 %d입니다.' % (s, d, min_cost(s, d, cost)))
