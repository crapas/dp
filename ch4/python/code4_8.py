
def max_sub_array_sum(arr, n):
    # C 예제의 INT_MIN과 같이 충분히 작은 값을 파이썬에서는
    # -float('inf')로 지정해 사용할 수 있습니다.
    max_sum = -float('inf')
    
    for i in range(0, n):
        temp_sum = 0
        for j in range(i, n):
            temp_sum += arr[j]
            if temp_sum > max_sum:
                max_sum = temp_sum
    return max_sum

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(arr)
print('부분 배열의 합의 최댓값은 %d입니다.' % max_sub_array_sum(arr, n))