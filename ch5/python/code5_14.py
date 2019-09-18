# 참고로 각 금액마다 메모를 제공해야 하는 이 예제는 메모 사용이 제한적일 수
# 있습니다. 예를 들어서 (가능성은 낮지만) 1억 원에 대해서 계산을 해야 하면 
# 1억 개의 원소를 가진 리스트 크기만큼의 메모리가 필요합니다.

def minCoins(coin, N, S):
  # resultArray[i]에는 i원을 거슬러줄 때 필요한 최소 동전의 
  # 개수를 저장합니다. 마지막에 resultArray[S]를 반환합니다.
  # 최솟값을 구하기 위해서 충분히 큰 값으로 초기화하면 되는데
  # 동전의 개수는 구하려는 금액(S)보다 클 수 없으므로 S의 값으로
  # 초기화합니다.
  resultArray = [S + 1] * (S + 1)

  # S = 0일 때. 
  resultArray[0] = 0

  # 1원부터 계산해 올라갑니다.
  for i in range(1, S + 1):
    for j in range(0, N):
      # 현재 구하려는 금액보다 작은 액면가의 동전에 대해서만 검사
      if coin[j] <= i:
        temp = resultArray[i - coin[j]]
        if (temp != S + 1) and (temp + 1 < resultArray[i]):
          resultArray[i] = temp + 1

  return resultArray[S]

coin = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
N = len(coin)
S = 997
print('%d원을 지불할 때 최소 동전의 개수는 %d개입니다.' % (S, minCoins(coin, N, S)))