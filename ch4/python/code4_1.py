M = 3
N = 4

# 행렬의 왼쪽 위가 (0, 0), 오른쪽 아래가 (m, n) 셀로 0부터 시작하므로
# 이 MxN 크기의 행렬이 주어졌을 때 m = M - 1, n = N - 1이 됩니다.
# cost 행렬을 배열로 선언하거나 함수를 호출할 때 주의합시다.
def min_path_cost(cost, m, n):
    x = min_path_cost(cost, m - 1, n)
    y = min_path_cost(cost, m, n - 1)
    return min(x, y) + cost[m][n]

cost = [[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]
print('최소 이동 비용은 %d입니다.' % min_path_cost(cost, M - 1, N - 1))