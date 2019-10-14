S_MAX = 997
resultArray = [-1] * (S_MAX + 1)

# 옮긴이_ 책의 코드는 메모를 사용하지 않았지만, 깃허브 예제는 메모를 사용해
# 구현해 제공합니다.
# 참고로 각 금액마다 메모를 제공해야 하는 이 예제는 메모 사용이 제한적일 수
# 있습니다. 예를 들어서 (가능성은 낮지만) 1억 원에 대해서 계산을 해야 하면 
# 1억 개의 원소를 가진 리스트 크기만큼의 메모리가 필요합니다.
# 여기서는 997원을 상한으로 가정하고 있습니다.
# 참고로 파이썬은 중첩 가능한 재귀 호출의 개수를 제한하는데, 기본값이 1000
# 입니다. 이 값은 sys.setrecursionlimit() 함수로 증가시킬 수 있지만, 이 역시
# 한계가 있습니다.

def minCoins(coin, N, S):
  # 종료 조건
  if S == 0:
    return 0
  
  if resultArray[S] != -1:
    return resultArray[S]

  # 최솟값을 저장하는 변수입니다.
  result = S_MAX
  for i in range(0, N):
    # 액면가가 S보다 같거나 작은 모든 동전에 대해서 재귀 호출합니다.
    if coin[i] <= S:
      temp = minCoins(coin, N, S - coin[i])

      # 지금까지의 최솟값보다 더 작으면 최솟값을 교체
      if temp + 1 < result:
        result = temp + 1
  
  resultArray[S] = result
  return result

coin = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
N = len(coin)
S = 997 # 997을 초과하면 오류 발생
print('%d원을 지불할 때 최소 동전의 개수는 %d개입니다.' % (S, minCoins(coin, N, S)))