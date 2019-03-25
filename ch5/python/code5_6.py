def isInterleaving(A, B, C):
  # A, B, C 세 문자열의 길이를 구합니다.
  M = len(A)
  N = len(B)
  lengthC = len(C)

  # A와 B 문자열의 길이의 합이 C 문자열의 길이와 다를 때
  if lengthC != M + N:
    return False

  # 간삽 여부를 저장하는 2차원 배열
  ilMatrix = [[True] * (N + 1) for i in range(0, M + 1)]

  # 첫번째 열을 채웁니다.
  for i in range(1, M + 1):
    if A[i - 1] != C[i - 1]:
      ilMatrix[i][0] = False
    else:
      ilMatrix[i][0] = ilMatrix[i - 1][0]

  # 첫번째 행을 채웁니다.
  for j in range(1, N + 1):
    if B[j - 1] != C[j - 1]:
      ilMatrix[0][j] = False
    else:
      ilMatrix[0][j] = ilMatrix[0][j - 1]
  
  # 나머지 셀을 채웁니다.
  for i in range(1, M + 1):
    for j in range(1, N + 1):
      currantA = A[i - 1]
      currentB = B[j - 1]
      currentC = C[i + j - 1]
      # C의 글자가 A의 글자와 같고 B의 글자와 다를 때
      if (currantA == currentC) and (currentB != currentC):
        ilMatrix[i][j] = ilMatrix[i - 1][j]
      # C의 글자가 B의 글자와 같고 A의 글자와 다를 때
      elif (currantA != currentC) and (currentB == currentC):
        ilMatrix[i][j] = ilMatrix[i][j - 1]
      # A, B, C 글자 모두가 같을 때
      elif (currantA == currentC) and (currentB == currentC):
        ilMatrix[i][j] = ilMatrix[i - 1][j] or ilMatrix[i][j - 1]
      else:
        ilMatrix[i][j] = False

  # 완성된 행렬을 출력합니다.
  for i in range(0, M + 1):
    for j in range(0, N + 1):
      print('%s' % 'T ' if ilMatrix[i][j] else 'F ', end = '')
    print()

  return ilMatrix[M][N]  

a = 'bcc'
b = 'bbca'
c = 'bbcbcac'
check = isInterleaving(a, b, c)
print('%s는 %s와 %s의 간삽' % (c, a, b), end = '')
if check:
  print('입니다.')
else:
  print('이 아닙니다.')