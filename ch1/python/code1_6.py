def tower_of_hanoi(s, d, e, n):
    if n <= 0:
      return
    tower_of_hanoi(s, e, d, n - 1)
    print('%d번 원반을 %c에서 %c로 옮깁니다.' % (n, s, d));
    tower_of_hanoi(e, d, s, n - 1)

n = int(input('원반의 수를 입력하세요 : '))
tower_of_hanoi('s', 'd', 'e', n)
