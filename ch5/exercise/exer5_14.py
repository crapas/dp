def knapsack(C, weight, value):
    n = len(value)

    # 도둑의 최대 이익을 저장하는 배열
    # dp[i][j]는 물건이 i개가 있고 배낭의 공간이 j일 때의 값입니다.
    dp = [[0] * (C + 1) for i in range(n + 1)]
    # 각 배낭 용량의 값 별로 최대로 훔쳐갈 수 있는 물건의 인덱스를 저장
    #   stolen_indices[(i, j)] -> 물건이 i 개가 있고, 배낭 용량이 J을 때의 장물의 인덱스 목록
    #   여러 조합이 있을 수 있으므로 리스트의 리스트입니다.
    stolen_indices = {}

    # 배낭의 공간이 0일 때 도둑은 아무것도 넣을 수 없습니다.
    for i in range(0, n + 1):
        dp[i][0] = 0
        stolen_indices[(i, 0)] = [[]]
    
    # 물건이 하나도 없을 때 도둑은 훔칠 게 없습니다.
    for j in range(0, C + 1):
        dp[0][j] = 0
        stolen_indices[(0, j)] = [[]]

    # 배열을 채워 넣습니다.
    for i in range(1, n + 1):
        for j in range(1, C + 1):            
            if weight[i - 1] <= j :
                x = j - weight[i - 1]
                # 아무 것도 넣지 않은 경우보다 현재의 물건을 넣은 경우의 가치가 더 큰 경우
                # 이 조합으로 변경합니다.
                if value[i - 1] + dp[i - 1][x] > dp[i - 1][j]:
                    dp[i][j] = value[i - 1] + dp[i - 1][x]
                    stolen_indices[(i, j)] = [stolen_index + [i - 1] for stolen_index in stolen_indices[(i - 1, x)]]
                    continue
                # 아무 것도 넣지 않은 경우와 현재의 물건을 넣은 가치가 같은 경우
                # 이 조합을 추가합니다. (동일 가치의 다른 가방 조합)
                elif value[i - 1] + dp[i - 1][x] == dp[i - 1][j]:
                    dp[i][j] = value[i - 1] + dp[i - 1][x]
                    stolen_indices[(i, j)] = stolen_indices[(i - 1, j)] + [stolen_index + [i - 1] for stolen_index in stolen_indices[(i - 1, x)]]
                    continue
            # 물건이 배낭의 용량보다 크거나 (따질 필요 없이 넣을 수 없음)
            # 물건을 배낭에 배낭에 어떤 식으로 넣어도 가치가 더 좋아지지 않는다면
            # 왼쪽 셀을 복사합니다.
            dp[i][j] = dp[i - 1][j]
            stolen_indices[(i, j)] = stolen_indices[(i - 1, j)]

    # 도둑의 이익표를 출력해봅시다.
    for i in range(0, n + 1):
        for j in range(0, C + 1):
            print('%3d' % dp[i][j], end='')
        print()

    return dp[n][C], stolen_indices[(n, C)]

weight = [2, 3, 4, 5]
value = [3, 4, 5, 6]
bag_size = 5
max_profit, stolen_idx = knapsack(bag_size, weight, value)
print('도둑이 가지고 갈 수 있는 가치의 최댓값은 %d입니다.' % max_profit)
print('이때 도둑이 훔친 물건의 index는 다음과 같습니다. -', stolen_idx)

# 최대 가치의 도둑질 방법이 두 가지 이상인 경우
weight = [2, 4, 4, 5]
value = [3, 4, 4, 6]
bag_size = 11
max_profit, stolen_idx = knapsack(bag_size, weight, value)
print('도둑이 가지고 갈 수 있는 가치의 최댓값은 %d입니다.' % max_profit)
print('이때 도둑이 훔친 물건의 index는 다음과 같습니다. -', stolen_idx)