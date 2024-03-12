
# n층의 빌딩, x개의 달걀
def egg_drop_trial(n, x):
    # 0층은 0번, 1층은 1번 던져보면 되며,
    # 만약 달걀이 1개인 경우 1층부터 꼭대기까지 n번 던져봐야 합니다.
    if n == 1 or n == 0 or x == 1:
        return n

    min_trial = float('inf')

    for p in range(1, n + 1):
        broken = egg_drop_trial(p - 1, x - 1) # 깨진 경우 - 아래층으로
        not_broken = egg_drop_trial(n - p, x)  # 깨지지 않은 경우 - 위층으로
        # 최악의 경우이므로 두 경우 중 큰 값이 필요합니다.
        this_trial = broken if broken > not_broken else not_broken
        # 최악의 경우의 최솟값이므로 최솟값을 구합니다.
        min_trial = this_trial if min_trial > this_trial else min_trial

    # 1번 던진 후의 결과이므로 1을 더해서 반환합니다.
    return min_trial + 1  

n, x = input('빌딩의 층수와 달걀의 개수를 입력하세요 : ').split()
n = int(n)
x = int(x)
print('%d층의 빌딩과 %d개의 달걀이 있을 때 최악의 경우 최소 %d회 떨어뜨려야 합니다.' % \
       (n, x, egg_drop_trial(n, x)))
