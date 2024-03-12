def longest_bitonic(arr):
    if not arr:
        return []
    
    # dp_inc는 배열의 해당 위치에서 종료되는 가장 긴 단조 증가 부분 수열의 길이를 저장합니다.
    # dp_r_inc는 역순 배열의 해당 위치에서 종료되는 가장 긴 단조 증가 부분 수열의 길이를 저장합니다.
    dp_inc = [1 for _ in range(len(arr))]
    dp_r_inc = [1 for _ in range(len(arr))]
    r_arr = arr[::-1]

    for i in range(len(arr)):
        for j in range(i):
            if arr[j] <= arr[i] and dp_inc[j] + 1 > dp_inc[i]:
                dp_inc[i] = dp_inc[j] + 1
            if r_arr[j] <= r_arr[i] and dp_r_inc[j] + 1 > dp_r_inc[i]:
                dp_r_inc[i] = dp_r_inc[j] + 1
    # dp_r을 다시 역순으로 뒤집으면, 해당 위치에서 시작하는 가장 긴 단조 감소 부분 
    # 수열의 길이가 됩니다.
    dp_dec = dp_r_inc[::-1]

    # dp_inc와 dp_dec의 대응되는 각 원소를 합친 후 1을 빼면 해당 인덱스의 위치에서 
    # 최대값을 가지는 바이토닉 부분 수열의 최대 길이가 됩니다.
    longest_bitonic_length = [dp_inc[i] + dp_dec[i] - 1 for i in range(len(arr))]

    return max(longest_bitonic_length)

# 가장 긴 바이토닉 부분 순열은 연습문제 5_10을 참조해서 같은 방법으로 위의 코드에
# 각 지점에서 끝나는 가장 긴 단조 증가 부분 수열과 각 지점에서 시작하는 가장 긴 단조
# 감소 부분 수열을 찾을 수 있습니다.
# 가장 긴 바이토닉 부분 수열을 구성하는 인덱스를 기준으로 둘을 겹치는 원소를 한 번
# 제외 시키면서 합치면 가장 긴 바이토닉 부분 수열을 찾을 수 있습니다.

# 연습문제 5_12의 예제 코드는 생략합니다. 아래 예시의 arr에 대해서
#   [1, 3, 9, 12, 4, 2]
#   [1, 2, 9, 12, 4, 2]
#   [1, 3, 9, 12, 7, 6]
#   [1, 2, 9, 12, 7, 6]
# 네 개의 결과를 모두 얻을 수 있도록 연습해 봅시다.

arr = [1, 3, 2, 9, 12, 4, 2, 7, 6, 10]
print("가장 긴 바이토닉 부분 수열의 길이 :", longest_bitonic(arr))
