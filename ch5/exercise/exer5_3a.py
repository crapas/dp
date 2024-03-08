# 메모이제이션 + 하향식 코드
def num_of_paths_topdown(m, n, memo = None):
    if memo is None:
        memo = {}
    if (m == 0) or (n == 0):
        return 1
    if (m, n) in memo:
        return memo[(m, n)]
    memo[(m, n)] = num_of_paths_topdown(m - 1, n, memo) + \
                   num_of_paths_topdown(m, n - 1, memo) + \
                   num_of_paths_topdown(m - 1, n - 1, memo) # 대각선 방향 추가
    return memo[(m, n)]

# 상향식 코드
def num_of_paths_bottomup(m, n):
    cache = [[0] * n for i in range(0, m)]
    for i in range(0, m):
        for j in range(0, n):
            if (i == 0) or (j == 0):
                cache[i][j] = 1
            else:
                cache[i][j] = cache[i - 1][j] + \
                              cache[i][j - 1] + \
                              cache[i - 1][j - 1] # 대각선 방향 추가

    return cache[m - 1][n - 1]

M, N = input('방의 구조를 입력하세요 : ').split()
M = int(M)
N = int(N)
print('총 경로의 수는 %d개입니다.' % num_of_paths_topdown(M - 1, N - 1))
print('총 경로의 수는 %d개입니다.' % num_of_paths_bottomup(M, N))