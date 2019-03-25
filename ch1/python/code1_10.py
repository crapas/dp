def bubbleSort(arr, n):
  for i in range(0, n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp

a = [10, 2, 6, 4, 5, 3, 2, 8]
print('원래 순서 : ', end = '')
print(a)
bubbleSort(a, 8)
print('정렬 결과 : ', end = '')
print(a)