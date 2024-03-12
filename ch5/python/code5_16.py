# value[i]는 길이 i인 철근의 가격입니다.
def max_value(value, N, memo = None):  
    if memo == None:
        memo = [-float('inf')] * N
    if N <= 0:
        return 0
    

    # 이미 계산된 값이 있으면 그 값을 반환
    if memo[N - 1] != -float('inf'):
        return memo[N - 1]

    for i in range(1, N + 1):
        memo[N - 1] = max(memo[N - 1], \
                        value[i] + max_value(value, N - i, memo))
    
    return memo[N - 1]

# 예제에 모호한 부분이 있습니다.
# 만약, 철근의 길이별 가격표가 8까지만 정해져 있는데, 잘라서 팔아야 할 철근의 길이가 10이라면 위의 구현은 틀린 구현이 됩니다.
# value[i] 대신 작은 값에 대해서도 아래처럼 재귀 호출로 구합니다. 이 때 value[i]의 값을 범위 내에서는 초기값으로 사용합니다.

def max_value2(value, N, memo = None):
    if memo == None:
        memo = [-float('inf')] * N
    if N <= 0:
        return 0

    # 이미 계산된 값이 있으면 그 값을 반환
    if memo[N - 1] != -float('inf'):
        return memo[N - 1]

    if N < len(value):
        memo[N - 1] = value[N]

    for i in range(1, N + 1):
        memo[N - 1] = max(memo[N - 1], \
                        max_value2(value, i, memo) + max_value2(value, N - i, memo))
    return memo[N - 1]


value = [0, 1, 5, 8, 9, 10, 17, 17, 20]
for N in range(9):
    print('길이 %d인 철근을 잘라서 팔 때 최대 %d의 이익을 얻을 수 있습니다.' % \
           (N, max_value(value, N)))
for N in range(12):
    print('길이 %d인 철근을 잘라서 팔 때 최대 %d의 이익을 얻을 수 있습니다.' % \
           (N, max_value2(value, N)))  