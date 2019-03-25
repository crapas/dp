ENOUGH_MAX = 99999999

def getMax(a, b):
  return a if a > b else b

# n층의 빌딩, x개의 달걀
def eggDropTrial(n, x):
  # trialCount[i][j]는 j층의 빌딩에서 i개의 달걀을 사용할 때
  # 필요한 최소 낙하 횟수를 저장합니다. 달걀이 0개일 때는 고려할 
  # 필요가 없으므로 trialCount[n][x + 1]로 정의해도 되지만
  # 이러면 층수 인덱스와 체계가 달라서 코드를 이해하기 어려우므로
  # 코드의 가독성을 위해 아래와 같이 정의합니다.
  trialCount = [[0] * (n + 1) for i in range(0, x + 1)]

  # 0층은 0번, 1층은 1번 던져보면 됩니다.
  for i in range(1, x + 1):
    trialCount[i][0] = 0
    trialCount[i][1] = 1

  # 달걀이 1개일 때는 항상 층 수 만큼 던져야 합니다.
  for j in range(1, n + 1):
    trialCount[1][j] = j
  
  # 배열의 나머지를 채웁니다.
  for i in range(2, x + 1):
    for j in range(2, n + 1):
      trialCount[i][j] = ENOUGH_MAX
      for k in range(1, j + 1):
        # (달걀이 깨진 경우) i - 1개의 달걀로 k - 1층 까지의 시행 횟수와
        # (달걀이 깨지지 않은 경우) i개의 달걀로 j - k층 까지의 시행 횟수
        # 두 값 중 더 큰 값이 최악의 경우입니다.
        thisTrial = 1 + getMax(trialCount[i - 1][k - 1], \
                               trialCount[i][j - k])
        # 최악의 경우의 최소값을 구해야 합니다.
        if thisTrial < trialCount[i][j]:
          trialCount[i][j] = thisTrial

  # 완성된 trialCount를 출력해 봅니다.
  for i in range(1, x + 1):
    for j in range(0, n + 1):
      print('%3d' % trialCount[i][j], end = '')
    print()

  return trialCount[x][n]

n, x = input('빌딩의 층수와 달걀의 개수를 입력하세요 : ').split()
n = int(n)
x = int(x)
print('%d층의 빌딩과 %d개의 달걀이 있을 때 최악의 경우 최소 %d회 떨어뜨려야 합니다.' % \
       (n, x, eggDropTrial(n, x)))
