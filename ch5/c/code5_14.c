#include <stdio.h>
#include <limits.h>

int minCoins(int *coin, int N, int S){
  // resultArray[i]에는 i원을 거슬러줄 때 필요한 최소 동전의
  // 개수를 저장합니다. 마지막에 resultArray[S]를 반환합니다.
  int resultArray[S + 1];

  // S = 0일 때
  resultArray[0] = 0;

  // 최소값을 구하기 위해 resultArray의 모든 값을 매우 큰 값으로 초기화합니다.
  for(int i = 1; i <= S; i++)
    resultArray[i] = INT_MAX;

  // 1원부터 계산해 올라갑니다.
  for(int i = 1; i <= S; i++)
  {
    for(int j = 0; j < N; j++)
    {
      // 현재 구하려는 금액보다 작은 액면가의 동전에 대해서만 검사
      if(coin[j] <= i)
      {
        int temp = resultArray[i - coin[j]];
        if(temp != INT_MAX && temp + 1 < resultArray[i])
          resultArray[i] = temp + 1;
      }
    }
  }
  return resultArray[S];
}

int main()
{
  int coin[] = {1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000};
  int N = sizeof(coin) / sizeof(int);
  int S = 42315;
  printf("%d원을 지불할 때 최소 동전의 개수는 %d개 입니다.\n", S, minCoins(coin, N, S));
  return 0;
}