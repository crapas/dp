from random import *

# 완전 탐색으로 계산
def maxSubStringLength(str):
  n = len(str)
  maxLen = 0

  # i = 부분 문자열의 시작 인덱스
  for i in range(0, n):
    # j = 부분 문자열의 끝 인덱스 (짝수 길이)
    for j in range(i + 1, n, 2):
      # length = 현재 부분 문자열의 길이
      length = j - i + 1

      # 만약 지금까지의 maxLen이 검사하려는 문자열보다 길면
      # 현재 문자열을 검사(앞쪽과 뒤쪽 절반의 숫자의 합이 같은지)하지 않습니다.
      if maxLen >= length:
        continue      
      lSum = 0
      rSum = 0
      for k in range(0, int(length / 2)):
        lSum += int(str[i + k])
        rSum += int(str[i + k + int(length / 2)])
      if lSum == rSum:
        maxLen = length
  return maxLen

# 다이나믹 프로그래밍으로 계산
def maxSubStringLength2(str):
  n = len(str)
  maxLen = 0
  # sum[i][j] = 인덱스 i에서 인덱스 j까지의 숫자의 합
  # i > j인 경우에는 사용하지 않습니다.
  sum = [[0] * n for i in range(0, n)]


  # 행렬의 대각선 아래쪽(i > j)은 사용하지 않습니다.
  # 대각선 위치의 값을 채워 넣습니다.
  for i in range(0, n):
    sum[i][i] = int(str[i])

  for length in range(2, n + 1):
    # 현재 부분 문자열의 i와 j를 선택합니다.
    for i in range(0, n - length + 1):
      j = i + length - 1
      k = int(length / 2)
      # sum[i][j]의 값을 계산
      sum[i][j] = sum[i][j - k] + sum[j - k + 1][j]
      # length가 짝수이고, 왼쪽과 오른쪽 절반의 합이 같으며 
      # length가 maxLen보다 크면 maxLen을 갱신합니다.
      if (length % 2 == 0) and (sum[i][j - k] == sum[j - k + 1][j]) and length > maxLen:
        maxLen = length
  return maxLen

n = int(input('생성할 숫자열의 길이를 입력하세요 : '))

# 길이 n의 무작위 난수 숫자열을 만듭니다.
numstr = str(randint(1, 9))
for x in range(1, n):
  numstr += str(randint(0, 9))

print('생성된 숫자열 : %s' % numstr)

result1 = maxSubStringLength(numstr)
result2 = maxSubStringLength2(numstr)

print('[완전 탐색] 결과 : %d' % result1)
print('[다이나믹 프로그래밍] 결과 : %d' % result2)
