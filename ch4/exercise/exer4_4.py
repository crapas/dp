def ways_to_score(n):
    #scores = [3, 5, 10]
    scores = [3, 5, 10]
    # 각 점수 별 경우의 수를 저장할 리스트를 초기화합니다.
    dp = [0] * (n + 1)
    # 0점까지의 경우의 수는 아무것도 하지 않는 1가지입니다.
    dp[0] = 1
    # 각 점수에 대해서 반복합니다.
    for score in scores:
        # 각 점수 별로 경우의 수를 계산합니다.
        # i - k점에서 k점에 도달할 수 있으므로 이전 경우의 수를 더해 나갑니다.
        for i in range(score, n + 1):
            dp[i] += dp[i - score]

    return dp[n]

N = int(input('목적 점수를 입력하세요 : '))
print('%d점까지의 경우의 수는 %d입니다.' % (N, ways_to_score(N)))