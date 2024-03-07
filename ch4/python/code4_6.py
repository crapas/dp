def ways_to_score(n):
    if n < 0:
      return 0
    if n == 0:
        return 1
    return ways_to_score(n - 10) \
          + ways_to_score(n - 5) \
          + ways_to_score(n - 3)

N = int(input('목적 점수를 입력하세요 : '))
print('%d점까지의 경우의 수는 %d입니다.' % (N, ways_to_score(N)))