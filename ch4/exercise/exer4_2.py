def count_ways_memo(n, memo = None):
    if memo is None:
        memo = {}
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo:
        memo[n] = count_ways_memo(n - 1, memo) + count_ways_memo(n - 2, memo)
    return memo[n]

def count_ways_bottonup(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n - 1]

n = int(input('공간의 가로 길이를 입력하세요 : '))
print('%dx2 공간에 타일을 놓을 수 있는 경우의 수는 %d입니다.(메모이제이션)' % (n, count_ways_memo(n)))
print('%dx2 공간에 타일을 놓을 수 있는 경우의 수는 %d입니다.(상향식)' % (n, count_ways_memo(n)))