def LPS_length(string, start, end):
  # 종료 조건 : start >= end
  if start > end:
    return 0
  if start == end:
    return 1

  # 첫 글자와 끝 글자가 같을 때
  if string[start] == string[end]:
    return LPS_length(string, start + 1, end - 1) + 2
  else:
    left = LPS_length(string, start, end - 1)
    right = LPS_length(string, start + 1, end)
    return left if left > right else right

string = 'BBABCBCAB'
start = 0
end = len(string) - 1
print('%s의 최대 회문 부분 수열의 길이는 %d입니다.' % \
  (string, LPS_length(string, start, end)))