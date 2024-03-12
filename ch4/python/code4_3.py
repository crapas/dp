def min_path_cost(cost, m, n, memo = None):
# 결과를 저장(메모)할 메모 변수 초기화
    if memo == None:
        memo = {}
    # 만약 셀 (m, n)의 최소 이동 비용이 이미 계산되어 있다면
    # 다시 계산하지 않습니다.
    if (m, n) in memo:
        return memo[(m, n)]
  
    if m == 0 and n == 0:
        memo[(m, n)] = cost[0][0]
    elif m == 0:                
        memo[(m, n)] = min_path_cost(cost, 0, n - 1) + cost[0][n]
    elif n == 0:                
        memo[(m, n)] = min_path_cost(cost, m - 1, 0) + cost[m][0]
    else:
        x = min_path_cost(cost, m - 1, n)
        y = min_path_cost(cost, m, n - 1)    
        memo[(m, n)] = min(x, y) + cost[m][n]
    return memo[(m, n)]

cost = [
    [1, 3, 5, 8], 
    [4, 2, 1, 7], 
    [4, 3, 2, 3]
]

M = len(cost)
N = len(cost[0])
print('최소 이동 비용은 %d입니다.' % min_path_cost(cost, M - 1, N - 1))