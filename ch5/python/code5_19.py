def knapsack(C, weight, value):
    n = len(value)

    # 도둑의 최대 이익을 저장하는 배열
    # dp[i][j]는 물건이 i개가 있고 배낭의 공간이 j일 때의 값입니다.
    dp = [[0] * (C + 1) for i in range(n + 1)]

    # 배낭의 공간이 0일 때 도둑은 아무것도 넣을 수 없습니다.
    for i in range(0, n + 1):
        dp[i][0] = 0
    
    # 물건이 하나도 없을 때 도둑은 훔칠 게 없습니다.
    for j in range(0, C + 1):
        dp[0][j] = 0

    # 배열을 채워 넣습니다.
    for i in range(1, n + 1):
        for j in range(1, C + 1):
            if weight[i - 1] <= j:
                x = j - weight[i - 1]
                dp[i][j] = max(value[i - 1] + dp[i - 1][x], dp[i - 1][j])
            else: # 물건이 배낭의 용량보다 크면 따질 필요 없이 왼쪽 셀을 복사합니다.
                dp[i][j] = dp[i - 1][j]

    # 도둑의 이익표를 출력해봅시다.
    for i in range(0, n + 1):
        for j in range(0, C + 1):
            print('%3d' % dp[i][j], end='')
        print()

    return dp[n][C]

weight = [2, 3, 4, 5]
value = [3, 4, 5, 6]
backsize = 5
print('도둑이 가지고 갈 수 있는 가치의 최댓값은 %d입니다.' % \
      knapsack(backsize, weight, value))
