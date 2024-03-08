# 예제의 그림에서 (4, 7)에서 (5, 7)로 가는 경로가 차단되어 있으므로
# (5, 7)까지의 경로의 수는 (5, 6)까지의 경로의 수와 동일합니다.
# 이러한 조건을 코드에 추가하기 위해서 blocks 딕셔너리를 추가하고, 이를 사용하여 계산합니다.
# 예제의 그림에는 가로 경로만 차단이 되어 있는데 아래 코드와 같이 차단 경로를 정의하면
# 세로 경로가 차단이 되어 있는 경우도 계산할 수 있습니다.
# 단 가로, 세로가 모두 차단된 경우는 계산할 튜플 대신 0으로 설정합니다.
def num_of_paths_topdown(m, n, blocks, memo = None):
    if memo is None:
        memo = {}
    if (m == 0) or (n == 0):    # 좌표 축 상의 점
        return 1
    if (m, n) in memo:          # 메모이제이션 확인
        return memo[(m, n)]
    
    # 재귀 호출
    # 만약 차단된 도로를 지나서 도착하는 좌표의 경우는
    #   모든 방향이 차단되어 있으면 0 (갈 수 없음)
    #   한쪽 방향이 차단되어 있으면 나머지 방향만 반영합니다.
    if (m, n) in blocks:
        if blocks[(m, n)] == 0:
            return 0
        else:
            return num_of_paths_topdown(blocks[(m, n)][0], blocks[(m, n)][1], blocks, memo)

    memo[(m, n)] = num_of_paths_topdown(m - 1, n, blocks, memo) + num_of_paths_topdown(m, n - 1, blocks, memo)
    return memo[(m, n)]

def num_of_paths_bottomup(m, n, blocks):
    cache = [[0] * (n + 1) for i in range(0, m + 1)]
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            # 차단된 도로를 지나서 도착하는 좌표의 경우는
            #   모든 방향이 차단되어 있으면 0 (갈 수 없음)
            #   한쪽 방향이 차단되어 있으면 나머지 방향만 반영합니다.
            if (i, j) in blocks:
                if blocks[(i, j)] == 0:
                    cache[i][j] = 0
                else:
                    cache[i][j] = cache[blocks[(i, j)][0]][blocks[(i, j)][1]]
            # 좌표 축 상의 점
            elif i == 0:
                if j == 0:
                    cache[0][0] = 1
                else:
                    cache[i][j] = cache[i][j - 1]
            elif j == 0:
                cache[i][j] = cache[i - 1][j]
            # 좌표 축이 아닌 점의 상향식 계산
            else:
                cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
    
    return cache[m][n]

blocks = {}
# (2, 1)에서 (3, 1) 경로가 차단되어 있으므로
# (3, 1)까지의 경로의 수는 (3, 0)까지의 경로의 수와 동일하다는 의미입니다.
blocks[(3, 1)] = (3, 0) 
blocks[(9, 1)] = (9, 0)
blocks[(2, 2)] = (2, 1)
blocks[(3, 2)] = (3, 1)
blocks[(4, 3)] = (4, 2)
blocks[(7, 3)] = (7, 2)
blocks[(3, 5)] = (3, 4)
blocks[(7, 6)] = (7, 5)
blocks[(5, 7)] = (5, 6)
blocks[(9, 7)] = (9, 6)
blocks[(2, 8)] = (2, 7)
blocks[(8, 10)] = (8, 9)

x, y = 10, 10
print('총 경로의 수는 %d개입니다.(메모이제이션)' % num_of_paths_topdown(x, y, blocks))
print('총 경로의 수는 %d개입니다.(하향식)' % num_of_paths_bottomup(x, y, blocks))
