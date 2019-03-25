def towerOfHanoi(s, d, e, n):
  if n <= 0:
    return
  towerOfHanoi(s, e, d, n - 1)
  print('%d번 원반을 %c에서 %c로 옮깁니다.' % (n, s, d));
  towerOfHanoi(e, d, s, n - 1)

n = int(input('원반의 수를 입력하세요 : '))
towerOfHanoi('s', 'd', 'e', n)
