# 메모이제이션과 마찬가지로 자를 대상인 철근의 길이의 제한이 없도로 예제 코드를 수정하였습니다.
# value[i]는 길이 i인 철근의 가격입니다.
def max_value(value, N):
    # dp[i] : 길이 i인 철근을 팔 때의 최대 이익 (C 구현의 maxValues)
    dp = [-float('inf')] * (N + 1)

    # value 범위 내의 철근의 경우, dp 배열이 초기값은 value와 동일하게 초기화합니다.
    for i in range(min(len(value), N + 1)):
        dp[i] = value[i]

    # 길이 1에서 N까지 계산해 올라갑니다.
    for i in range(1, N + 1):
        # 길이 i인 철근은 i 길이에 해당되는 토막 가격(dp[i])까지만 필요합니다.
        for j in range(1, i + 1):
            # i - j 길이의 최대 이익에 j 길이의 철근의 가격을 더하면 i 길이 철근의
            # 판매 가격을 구할 수 있으며, 모든 j에 대해서 최댓값을 취하면
            # 길이 i인 철근을 판매할 때의 최대 이익을 구할 수 있습니다.
            dp[i] = max(dp[i], dp[j] + dp[i - j])
    
    # 완성된 배열을 출력해봅니다.
    for i in range(0, N + 1):
        print('%3d' % dp[i], end = '')
    print()

    return dp[N]

value = [0, 1, 5, 8, 9, 10, 17, 17, 20]
for N in range(12):
    print('길이 %d인 철근을 잘라서 팔 때 최대 %d의 이익을 얻을 수 있습니다.' % \
        (N, max_value(value, N)))
  