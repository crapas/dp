# 연습문제 5-2에서 대각선 방향이 추가되면, 차단되는 경우가 세 방향 모두
# 두 방향, 한 방향 이렇게 다양한 경우로 늘어납니다.
# 그러므로 blocks 딕셔너리의 값을 튜플의 리스트로 바꾸어서 튜플의 리스트에
# 해당하는 가능한 경로를 더하도록 수정합니다.
# 세방향이 모두 차단된 경우는 빈 리스트로 지정하면 됩니다.

def num_of_paths_topdown(m, n, blocks, memo = None):
    if memo is None:
        memo = {}
    if (m == 0) or (n == 0):    # 좌표 축 상의 점
        return 1
    if (m, n) in memo:          # 메모이제이션 확인
        return memo[(m, n)]
    
    # 재귀 호출
    # 차단된 도로를 지나서 도착하는 좌표의 경우는
    #   차단되지 않은 이전 점으로 구성된 튜플의 리스트에 해당하는 값만 더합니다.
    if (m, n) in blocks:
        memo[(m, n)] = 0
        for possible in blocks[(m, n)]:
            memo[(m, n)] += num_of_paths_topdown(possible[0], possible[1], blocks, memo)
        return memo[(m, n)]

    memo[(m, n)] = num_of_paths_topdown(m - 1, n, blocks, memo) + \
                   num_of_paths_topdown(m, n - 1, blocks, memo) + \
                   num_of_paths_topdown(m - 1, n - 1, blocks, memo) # 대각선 방향
    return memo[(m, n)]

def num_of_paths_bottomup(m, n, blocks):
    cache = [[0] * (n + 1) for i in range(0, m + 1)]
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            # 차단된 도로를 지나서 도착하는 좌표의 경우는
            #   차단되지 않은 이전 점으로 구성된 튜플의 리스트에 해당하는 값만 더합니다.
            if (i, j) in blocks:
                cache[i][j] = 0
                for possible in blocks[(i, j)]:
                    cache[i][j] += cache[possible[0]][possible[1]]
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
                cache[i][j] = cache[i - 1][j] + \
                              cache[i][j - 1] + \
                              cache[i - 1][j - 1] # 대각선 방향
    
    return cache[m][n]

blocks = {}
# (3, 3)에서 (4, 3) 경로가 차단되어 있으므로
# (4, 3)까지의 경로의 수는 (4, 2)까지의 경로의 수와 (3, 2)까지의 경로의 수의 합입니다.
blocks[(4, 3)] = [(4, 2), (3, 2)]

blocks[(3, 1)] = [(3, 0), (2, 0)]
blocks[(9, 1)] = [(9, 0), (8, 0)]
blocks[(2, 2)] = [(2, 1), (1, 1)]
blocks[(3, 2)] = [(3, 1), (2, 1)]
blocks[(7, 3)] = [(7, 2), (6, 2)]
blocks[(3, 5)] = [(3, 4), (2, 4)]
blocks[(7, 6)] = [(7, 5), (6, 5)]
blocks[(5, 7)] = [(5, 6), (4, 6)]
blocks[(9, 7)] = [(9, 6), (8, 6)]
blocks[(2, 8)] = [(2, 7), (1, 7)]
blocks[(8, 10)] = [(8, 9), (7, 9)]

# 만약 차단된 도로가 둘 인 경우는 리스트에 열린 경로 하나만, 
# 모두 차단된 경우는 빈 리스트로 지정합니다.

x, y = 10, 10
print('총 경로의 수는 %d개입니다.(메모이제이션)' % num_of_paths_topdown(x, y, blocks))
print('총 경로의 수는 %d개입니다.(하향식)' % num_of_paths_bottomup(x, y, blocks))
