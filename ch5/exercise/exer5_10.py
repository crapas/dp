# 주어진 리스트에서 각 위치별로, 해당 위치에서 종료되는 가장 긴 단조 증가 부분 수열의 길이를 저장합니다.
# 최대 값이 갱신될 때, 이때의 이전 인덱스 j를 함께 저장해서 최장 길이 단조 증가 부분 순열을 만들 수 있도록 합니다.
def longest_increasing_subsequence(arr):    
    if not arr:
        return []

    # 단조 증가 부분 수열 길이의 최소값에 해당되는 1, 그리고 이전 인덱스를 알 수 없으므로 None으로 초기화합니다.
    dp = [(1, None) for _ in range(len(arr))]

    # 상향식으로 계산하는 과정에서
    # 현재 위치에서 끝나는 단조 증가 부분 수열의 이전 인덱스를 함께 저장합니다.
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] <= arr[i] and dp[j][0] + 1 > dp[i][0]:
                dp[i] = (dp[j][0] + 1, j)

    # lis가 가장 큰 위치를 찾습니다.    
    lis_length = -float('inf')
    lis_last_index = None
    
    for i in range(len(arr)):
        if lis_length < dp[i][0]:
            lis_length = dp[i][0]
            lis_last_index = i

    # 가장 큰 위치부터 이전 값들을 차례로 찾아서 목록을 채운 후
    lis = []
    while lis_last_index != None:
        lis += [arr[lis_last_index]]
        _, lis_last_index = dp[lis_last_index]
    # 뒤에서부터 찾아 채웠으므로 목록을 뒤집은 후 반환합니다.
    lis.reverse()
    return lis


arr = [7, 1, 5, 4, 2, 4, 9]
print(longest_increasing_subsequence(arr))

# 구현한 함수는 [1, 4, 4, 9]를 반환합니다. 각자 [[1, 2, 4, 9], [1, 4, 4, 9]] 두개 모두를 반환하도록 수정해봅시다.