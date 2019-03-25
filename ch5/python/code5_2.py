def getMinimum(a, b, c):
  return a if (a < b) and (a < c) else b if b < c else c

def editDistance(str1, str2, m, n):
  EditD = [[0] * (n + 1) for i in range(0, m + 1)]

  for j in range(0, n + 1):   # 제일 윗 행
    EditD[0][j] = j
  
  for i in range(0, m + 1):   # 제일 왼쪽 열
    EditD[i][0] = i

  for i in range(1, m + 1):
    for j in range(1, n + 1):
      # 두 글자가 같다면
      if str1[i - 1] == str2[j - 1]:
        EditD[i][j] = EditD[i - 1][j - 1]
      # 두 글자가 다르다면
      else:
        EditD[i][j] = getMinimum(EditD[i][j - 1], \
                                 EditD[i - 1][j], \
                                 EditD[i - 1][j - 1]) + 1

  # 완성된 EditD 행렬을 출력해 봅니다.
  for i in range(0, m + 1):
    for j in range(0, n + 1):
      print('%2d' % EditD[i][j], end = '')
    print()
  
  return EditD[m][n]

str1, str2 = input('두 단어를 입력하세요 : ').split()
print('두 단어 [%s] [%s] 사이의 최소 교정 비용은 %d 입니다.' % \
  (str1, str2, editDistance(str1, str2, len(str1), len(str2))))