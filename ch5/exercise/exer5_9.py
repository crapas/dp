# 주어진 리스트에서 각 위치별로, 해당 위치에서 종료되는 가장 긴 단조 증가 부분 수열의 길이를 저장합니다.
# 예를 들어 입력이 [7, 1, 5, 4, 2, 4, 9]일 때, dp 배열의 값은 [1, 1, 2, 2, 2, 3, 4]가 됩니다.
# 0 : [7]
# 1 : [7] 또는 [1]
# 2 : [1, 5]
# 3 : [1, 5] 또는 [1, 4]
# 5 : [1, 4, 4] 또는 [1, 2, 4]
# 6 : [1, 4, 4, 9] 또는 [1, 2, 4, 9]
def longest_increasing_subsequence_length(arr):
    if not arr:
        return []

    # 단조 증가 부분 수열 길이의 최소값에 해당되는 1로 초기화합니다.
    dp = [1 for _ in range(len(arr))]

    # 상향식으로 계산하는 과정에서
    # j < i이고  arr[j] <= arr[i]인 경우, 
    # arr[i]에서 끝나는 단조 증가 부분 순열에는 arr[j]가 포함될 수도 그렇지 않을 수도 있습니다.
    # arr[j]가 포함되는 경우는 dp[j] + 1의 값은 dp[i]보다 같거나 작아야 하며
    # (arr[j] 다음 1개 이상의 원소가 더 나온 후 arr[i]가 나오는 형태의 부분 수열)
    # arr[j]와 arr[i]가 붙어 있는 경우에는 dp[j] + 1 = dp[i]가 됩니다. 
    # 그러므로 이때 dp[j] + 1이 dp[i]보다 크면 dp[i]의 값을 갱신합니다.
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] <= arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1                
    return max(dp)

arr = [7, 1, 5, 4, 2, 4, 9]
print(longest_increasing_subsequence_length(arr))