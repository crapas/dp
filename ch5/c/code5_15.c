#include <stdio.h>
#include <limits.h>

// 두 수 중 큰 수를 반환하는 도우미 함수
int getMax(int a, int b)
{
  return a > b? a: b;
}

// value[i]는 길이 i인 철근의 가격입니다.
int maxValue(int *value, int N)
{
  // 종료 조건 : 남은 철근이 없을 때 
  if(N <= 0)
    return 0;

  // 최대 이익
  int price = INT_MIN;

  for(int i = 1; i <= N; i++)
  {
    price = getMax(price, 
                   value[i] + maxValue(value, N - i));
  }
  return price;
}

int main()
{
  int value[] = {0, 1, 5, 8, 9, 10, 17, 17, 20};
  int N = 8;
  printf("길이 %d인 철근을 잘라서 팔 때 최대 %d의 이익을 얻을 수 있습니다.\n", N, maxValue(value, N));
  return 0;
}