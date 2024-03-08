# Board size : N X N
# initial location : start (0, 0) ~ (N - 1, N - 1)
# destination : end (0, 0) ~ (N - 1, N - 1)


# 도우미 함수 : 항목이 2인 두 튜플의 대응되는 원소끼리 더한 결과를 반환합니다.
def tuple_sum(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

# 도우미 함수 : 주어진 지점이 가로 세로 N인 보드 내에 위치하는지 확인합니다.
def border_check(position, N):
    return position[0] >= 0 and position[1] >= 0 and position[0] < N and position[1] < N

# 상향식으로 계산합니다.
# 시작 지점으로부터 어떤 지점에 말이 도착했을 때, 그 때까지의 이동 횟수가 해당 칸의 기존 이동 횟수보다 작으면
# 더 작은 값으로 갱신하면서 모든 보드에 대해서 계산합니다.
# 다만 말은 자유롭게 이동할 수 있으므로 이 경우 무한 반복되기 때문에 종료 조건이 필요합니다.
# 종료 조건으로는, 현재 탐색하는 지점을 기준으로 이동 가능한 최대 16개의 목적지의 (가장자리 조건에 따라 일부 제외)
# 최소 이동 횟수를 이미 저장한 값과 비교해서 갱신하되, 만약 값이 바뀌면, 값이 바뀐 노드의 새로운 최소값으로
# 재탐색을 수행해야 하므로 큐를 사용해서 큐에 추가합니다.
# 큐에 저장된 노드를 하나씩 꺼내서 탐색을 하고, 큐가 빌 때 (즉 더 이상 보드에 갱신이 발생하지 않을 때) 까지 
# 반복합니다.
# 
# 단, 이 문제는 장기 말이 인접한 칸으로 이동할 수 있는 특수한 경우이므로 되돌아가는 경우는 고려할 필요가 없이
# 한 번 방문한 칸을 다시 방문하지 않고 값도 갱신되지 않도록 해도 같은 결과가 나옵니다. 하지만 체스의 나이트, 장기의
# 마나 상 같은 경우는 되돌아가는 경우도 고려해야 합니다.
from collections import deque
def minimal_move(N, start, end, moves):
    minimal_move = {}
    minimal_move[start] = 0
    changed_queue = deque([start])
    while changed_queue:
        current = changed_queue.popleft()
        for move in moves:
            next = tuple_sum(current, move)
            if border_check(next, N):
                if next not in minimal_move:
                    minimal_move[next] = float('inf')
                if minimal_move[next] > minimal_move[current] + 1:
                    minimal_move[next] = minimal_move[current] + 1
                    changed_queue.append(next)
    if end not in minimal_move:
        return None
    return minimal_move[end]


def minimal_move2(N, start, end, moves):
    x_direction = (end[0] - start[0]) // abs(end[0] - start[0])
    y_direction = (end[1] - start[1]) // abs(end[1] - start[1])
    minimal_move = {}
    minimal_move[start] = 0

    for i in range(start[0], end[0], x_direction):
        for j in range(start[1], end[1], y_direction):
            current = (i, j)
            for move in moves:
                next = tuple_sum(current, move)
                if border_check(next, N):
                    if next not in minimal_move:
                        minimal_move[next] = float('inf')
                    minimal_move[next] = min(minimal_move[next], minimal_move[current] + 1)
    return minimal_move[end]



N = 100
start = (86, 14)
end = (4, 99)

# 문제에서 제시한 마왕의 가능한 이동 방향입니다.
# 이런 특수한 말 (대각선까지 포함한 인접 8방향으로 이동 가능)의 경우에는 minimal_move2 함수와 같이
# 해당 방향으로 계산해 나가는 경우도 가능합니다.
moves = [
    (1, 2), (2, 1), (1, -2), (2, -1),
    (-1, 2), (-2, 1), (-1, -2), (-2, -1),
    (1, 0), (0, 1), (-1, 0), (0, -1),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
]

min_move = minimal_move(N, start, end, moves)
min_move2 = minimal_move2(N, start, end, moves)
print('(큐를 이용)%d회 만에 이동할 수 있습니다.' % min_move)
print('(상향식으로만)%d회 만에 이동할 수 있습니다.' % min_move2)

# 문제에서 제시하지 않았지만 체스의 나이트의 경우입니다.
moves =[ 
    (1, 2), (2, 1), (1, -2), (2, -1),
    (-1, 2), (-2, 1), (-1, -2), (-2, -1),
]
min_move = minimal_move(N, start, end, moves)
if min_move == None:
    print('이동이 불가능합니다.')
else:
    print('%d회 만에 이동할 수 있습니다.' % min_move)

# 말에 따라 이동이 불가능한 경우도 있습니다.
moves =[ 
    (1, 3), (3, 1), (1, -3), (3, -1),
    (-1, 3), (-3, 1), (-1, -3), (-3, -1),
]
min_move = minimal_move(N, start, end, moves)
if min_move == None:
    print('이동이 불가능합니다.')
else:
    print('%d회 만에 이동할 수 있습니다.' % min_move)
