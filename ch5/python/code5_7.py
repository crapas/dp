def is_subset_sum(arr, n, X):
    # 종료 조건 1 : X가 0이면 성공 종료 조건입니다.
    if X == 0:
        return True

    # 종료 조건 2 : X가 0이 아니고 남은 원소가 없다면 실패 종료 조건입니다.
    if n == 0:
        return False
    
    # X보다 큰 원소는 무시해도 좋습니다.
    if arr[0] > X:
        return is_subset_sum(arr[1:], n - 1, X)

    # 부분집합에 원소를 포함시키지 않는 경우와 
    # 원소를 포함시키는 경우 각각에 대해 재귀 호출합니다.
    return is_subset_sum(arr[1:], n - 1, X) or \
           is_subset_sum(arr[1:], n - 1, X - arr[0])    
         
arr = [0, 6, 11, 8, 17, 3, 9]
print('결과는 %s입니다.' % ('참' if is_subset_sum(arr, 7, 13) else '거짓'))
# [6, 8] 또는 [0, 6, 8]의 합은 14입니다.
print('결과는 %s입니다.' % ('참' if is_subset_sum(arr, 7, 14) else '거짓'))
