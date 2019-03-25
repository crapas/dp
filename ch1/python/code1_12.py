def bubbleSort(arr, n):
  # 종료 조건
  if n == 1:
    return
  # 1회의 탐색 과정을 수행
  for j in range(0, n - 1):
    if arr[j] > arr[j + 1]:
      temp = arr[j]
      arr[j] = arr[j + 1]
      arr[j + 1] = temp
  # 더 작은 범위의 인수로 재귀 호출   
  bubbleSort(arr, n - 1)

a = [10, 2, 6, 4, 5, 3, 2, 8]
print('원래 순서 : ', end = '')
print(a)
bubbleSort(a, 8)
print('정렬 결과 : ', end = '')
print(a)