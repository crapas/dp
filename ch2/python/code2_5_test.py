import time
from random import randint


# 출발역(s)에서 도착역(d)까지의 최소 요금을 계산합니다.
def min_cost(s, d, cost, memo = None):  
    if memo == None:
        memo = {}

    if s == d or s == d - 1:
        return cost[s][d]

    # 값이 계산되지 않은 경우에만 블록 안으로 들어가서 계산합니다.
    # 메모된 값이 없을 때
    if (s, d) not in memo:
        # 재귀 호출을 사용하는 코드와 메모이제이션을 제외하면 동일합니다.
        min_value = cost[s][d]

        for i in range(s + 1, d):
            cost_s_i_d = min_cost(s, i, cost, memo) + min_cost(i, d, cost, memo)
            min_value = min(min_value, cost_s_i_d)            
            # 계산된 최소 요금을 메모에 저장. 딕셔너리이므로 [][] 대신 [튜플]을 사용합니다.
            memo[(s, d)] = min_value      
    return memo[(s, d)]



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

s = 0
d = num_of_station - 1
start_time = int(round(time.time() * 1000))
print('%d번 역에서 %d번 역까지의 최소 비용은 %d입니다.' % (s, d, min_cost(s, d, cost)))
end_time = int(round(time.time() * 1000))
print('min_cost 함수의 실행 시간 : %d(ms)' % (end_time - start_time))