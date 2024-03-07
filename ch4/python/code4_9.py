
def max_sub_array_sum(arr, n):
    max_value = -float('inf')
    all_negative = True

    for i in range(0, n):
        if arr[i] >= 0:
            all_negative = False
            break
        elif arr[i] > max_value:
            max_value = arr[i]
    
    if all_negative:
        return max_value
    
    max_sum_so_far = 0
    max_sum_ending_here = 0

    for i in range(0, n):
        max_sum_ending_here += arr[i]

        if max_sum_ending_here < 0:
            max_sum_ending_here = 0
        
        if max_sum_so_far < max_sum_ending_here:
            max_sum_so_far = max_sum_ending_here
        # 표 4-1 확인을 위한 임시 값 출력
        print('i = %d, arr[i] = %2d, maxSumEndingHere : %2d, maxSumSoFar : %2d' % \
          (i, arr[i], max_sum_ending_here, max_sum_so_far))

    return max_sum_so_far

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(arr)
print('부분 배열의 합의 최댓값은 %d입니다.' % max_sub_array_sum(arr, n))