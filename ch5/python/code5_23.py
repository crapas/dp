# n층의 빌딩, x개의 달걀
def egg_drop_trial(n, x):
    # trial_count[i][j]는 j층의 빌딩에서 i개의 달걀을 사용할 때
    # 필요한 최소 낙하 횟수를 저장합니다. 달걀이 0개일 때는 고려할 
    # 필요가 없으므로 trial_count[n][x + 1]로 정의해도 되지만
    # 이러면 층수 인덱스와 체계가 달라서 코드를 이해하기 어려우므로
    # 코드의 가독성을 위해 아래와 같이 정의합니다.
    trial_count = [[0] * (n + 1) for i in range(0, x + 1)]

    # 0층은 0번, 1층은 1번 던져보면 됩니다.
    for i in range(1, x + 1):
        trial_count[i][0] = 0
        trial_count[i][1] = 1

    # 달걀이 1개일 때는 항상 층수만큼 던져야 합니다.
    for j in range(1, n + 1):
        trial_count[1][j] = j
    
    # 배열의 나머지를 채웁니다.
    for i in range(2, x + 1):
        for j in range(2, n + 1):
            trial_count[i][j] = float('inf')
            for k in range(1, j + 1):
                # (달걀이 깨진 경우) i - 1개의 달걀로 k - 1층까지의 시행 횟수와
                # (달걀이 깨지지 않은 경우) i개의 달걀로 j - k층까지의 시행 횟수
                # 두 값 중 더 큰 값이 최악의 경우입니다.
                this_trial = 1 + max(trial_count[i - 1][k - 1], \
                                    trial_count[i][j - k])
                # 최악의 경우의 최솟값을 구해야 합니다.
                if this_trial < trial_count[i][j]:
                    trial_count[i][j] = this_trial

    # 완성된 trialCount를 출력해봅니다.
    for i in range(1, x + 1):
        for j in range(0, n + 1):
            print('%3d' % trial_count[i][j], end = '')
        print()

    return trial_count[x][n]

n, x = input('빌딩의 층수와 달걀의 개수를 입력하세요 : ').split()
n = int(n)
x = int(x)
print('%d층의 빌딩과 %d개의 달걀이 있을 때 최악의 경우 최소 %d회 떨어뜨려야 합니다.' % \
       (n, x, egg_drop_trial(n, x)))
