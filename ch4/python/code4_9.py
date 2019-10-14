INT_MIN = -99999999

def maxSubArraySum(arr, n):
  # python3의 int 자료형은 상/하한이 없습니다. 
  # C 예제처럼 INT_MIN을 사용할 수 없으므로 충분히 작은 값을 
  # 임의로 정해 초기값으로 사용합니다.
  maxValue = INT_MIN
  allNegative = True

  for i in range(0, n):
    if arr[i] >= 0:
      allNegative = False
      break
    elif arr[i] > maxValue:
      maxValue = arr[i]
  
  if allNegative:
    return maxValue
  
  maxSumSoFar = 0
  maxSumEndingHere = 0

  for i in range(0, n):
    maxSumEndingHere += arr[i]

    if maxSumEndingHere < 0:
      maxSumEndingHere = 0
    
    if maxSumSoFar < maxSumEndingHere:
      maxSumSoFar = maxSumEndingHere

    print('i = %d, arr[i] = %2d, maxSumEndingHere : %2d, maxSumSoFar : %2d' % \
      (i, arr[i], maxSumEndingHere, maxSumSoFar))

  return maxSumSoFar

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(arr)
print('부분 배열의 합의 최댓값은 %d입니다.' % maxSubArraySum(arr, n))