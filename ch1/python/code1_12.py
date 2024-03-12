def bubble_sort(arr, n = None):
    if n == None:
        n = len(arr)
    # 종료 조건
    if n == 1 or n == 0:
        return
    # 1회의 탐색 과정을 수행
    for j in range(0, n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # 더 작은 범위의 인수로 재귀 호출   
    bubble_sort(arr, n - 1)

a = [10, 2, 6, 4, 5, 3, 2, 8]
print('원래 순서 : ', end = '')
print(a)
bubble_sort(a, 8)
print('정렬 결과 : ', end = '')
print(a)