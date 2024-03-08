# 이 문제는 코드 5-3, 5-4의 M X N 문제가 (x + 1) X (y + 1) 문제로 바뀐 경우와 동일합니다.
# 하향식 코드에는 메모이제이션을 추가한 예제를 보여 드립니다.
def num_of_paths_topdown(m, n, memo = None):
    if memo is None:
        memo = {}
    if (m == 0) or (n == 0):    # 좌표 축 상의 점
        return 1
    if (m, n) in memo:          # 메모이제이션 확인
        return memo[(m, n)]
    
    # 재귀 호출
    memo[(m, n)] = num_of_paths_topdown(m - 1, n, memo) + num_of_paths_topdown(m, n - 1, memo)
    return memo[(m, n)]

def num_of_paths_bottomup(m, n):
    cache = [[0] * (n + 1) for i in range(0, m + 1)]

    for i in range(0, m + 1):
        cache[i][0] = 1
    
    for j in range(0, n + 1):
        cache[0][j] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
    
    return cache[m][n]

x, y = 10, 10
print('총 경로의 수는 %d개입니다.(메모이제이션)' % num_of_paths_topdown(x, y))
print('총 경로의 수는 %d개입니다.(하향식)' % num_of_paths_bottomup(x, y))
