INT_MIN = -99999999

def maxSubArraySum(arr, n):
  # python3의 int 자료형은 상/하한이 없습니다. 
  # C 예제처럼 INT_MIN을 사용할 수 없으므로 충분히 작은 값을 
  # 임의로 정해 초기값으로 사용합니다.
  maxSum = INT_MIN
  
  for i in range(0, n):
    tempSum = 0
    for j in range(i, n):
      tempSum += arr[j]
      if tempSum > maxSum:
        maxSum = tempSum
  return maxSum

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(arr)
print('부분 배열의 합의 최대값은 %d입니다.' % maxSubArraySum(arr, n))