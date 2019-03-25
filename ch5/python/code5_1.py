def getMinimum(a, b, c):
  return a if (a < b) and (a < c) else b if b < c else c

def editDistance(str1, str2):
  # str1이 빈 문자열이면 str2의 모든 글자를 삽입하면 됩니다.
  if (str1 is None) or (len(str1) == 0):
    return len(str2)
  # str2가 빈 문자열일때도 마찬가지입니다.
  if (str2 is None) or (len(str2) == 0):
    return len(str1)

  # 첫번째 글자가 같을 때는 첫번째 글자를 무시하고
  # 나머지 단어 간의 최소 교정 비용을 구합니다.
  if str1[0] == str2[0]:
    return editDistance(str1[1:], str2[1:])

  # 삭제 연산 후 최소 교정 비용을 구하는 재귀 호출
  # 실제로 삭제하는 대신 str1의 첫번째 글자를 제외하고
  # 양쪽 단어 사이의 최소 교정 비용을 구합니다.
  d = editDistance(str1[1:], str2)
  # 치환 연산 후 최소 교정 비용을 구하는 재귀 호출
  # 치환 후 첫번째 글자가 같아지므로 실제로 치환하는 대신
  # 두번째 글자부터의 양쪽 단어 사이의 최소 교정 비용을 구합니다.
  u = editDistance(str1[1:], str2[1:])
  # 삽입 연산 후 최소 교정 비용을 구하는 재귀 호출
  # 실제로 삽입하는 대신 str2의 첫번째 글자를 제외하고
  # 양쪽 단어 사이의 최소 교정 비용을 구합니다.
  i = editDistance(str1, str2[1:])

  # 세 연산 이후 최소 교정 비용 간의 최소값에 1을 더해서 반환합니다.
  # getMinumum() 함수는 세 정수의 최소값을 구하는 도우미 함수입니다.
  return getMinimum(d, u, i) + 1

str1, str2 = input('두 단어를 입력하세요 : ').split()
print('두 단어 [%s] [%s] 사이의 최소 교정 비용은 %d 입니다.' % \
  (str1, str2, editDistance(str1, str2)))