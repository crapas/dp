#include <stdio.h>
#include <limits.h>
#define S_MAX 49999
int resultArray[S_MAX];

// 옮긴이_ 책의 코드는 메모를 사용하지 않았지만, 깃허브 예제는 메모를 사용해
// 구현해 제공합니다.
// 참고로 각 금액마다 메모를 제공해야 하는 이 예제는 메모 사용이 제한적일 수
// 있습니다. 예를 들어서 (가능성은 낮지만) 1억 원에 대해서 계산을 해야 하면 
// sizeof(int) * 1억만큼의 메모리가 필요합니다.
// 여기서는 49999원을 상한으로 가정하고 있습니다.

int minCoins(int *coin, int N, int S)
{
  // 종료 조건
  if(S == 0)
    return 0;
  
  if(resultArray[S] != -1)
    return resultArray[S];

  // 최솟값을 저장하는 변수입니다.
  int result = INT_MAX;
  for(int i = 0; i < N; i++)
  {
    // 액면가가 S보다 같거나 작은 모든 동전에 대해서 재귀 호출합니다.
    if(coin[i] <= S)
    {
      int temp = minCoins(coin, N, S - coin[i]);

      // 지금까지 최솟값보다 더 작으면 최솟값을 교체
      if(temp + 1 < result)
        result = temp + 1;
    }
  }
  resultArray[S] = result;
  return result;
}

int main()
{
  int coin[] = {1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000};
  int N = sizeof(coin) / sizeof(int);
  int S = 997;
  for(int i = 0; i <= S; i++)
    resultArray[i] = -1;
  printf("%d원을 지불할 때 최소 동전의 개수는 %d개입니다.\n", S, minCoins(coin, N, S));
  return 0;
}