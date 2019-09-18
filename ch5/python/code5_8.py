# n은 집합의 원소의 수입니다.
def isSubsetSum(arr, n, X):
  subsum = [[False] * (X + 1) for i in range(0, n)]

  # 첫번째 열은 항상 참
  for i in range(0, n):
    subsum[i][0] = True
  
  # 첫번째 행은 j가 0 또는 arr[0]인 경우만 참
  for j in range(1, X + 1):
    if arr[0] == j:
      subsum[0][j] = True
    else:
      subsum[0][j] = False

  # 나머지 셀을 채웁니다.
  for i in range(1, n):
    v = arr[i]
    for j in range(1, X + 1):
      if j < v:
        subsum[i][j] = subsum[i - 1][j]
      elif subsum[i - 1][j]:
        subsum[i][j] = True
      else:
        subsum[i][j] = subsum[i - 1][j - v]
  
  # 완성된 행렬을 출력해봅니다.
  for i in range(0, n):
    for j in range(0, X + 1):
      print('%s' % ('T ' if subsum[i][j] else 'F '), end = '')
    print()

  return subsum[n - 1][X]

arr = [0, 6, 11, 8, 17, 3, 9]
print('결과는 %s입니다.' % ('참' if isSubsetSum(arr, 7, 13) else '거짓'))
print('결과는 %s입니다.' % ('참' if isSubsetSum(arr, 7, 14) else '거짓'))
