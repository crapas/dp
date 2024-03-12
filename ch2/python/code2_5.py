# 이차원 배열 처럼 여러 차원으로 정의되는 값을 메모이제이션 하는 경우
# 튜플을 사용해 딕셔너리를 메모이제이션 변수로 사용할 수 있습니다.
# 아래 코드를 참고하세요.

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
