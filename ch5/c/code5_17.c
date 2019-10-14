#include <stdio.h>
#include <limits.h>

int getMax(int a, int b)
{
  return a > b? a: b;
}

// value[i]는 길이 i인 철근의 가격입니다.
int maxValue(int *value, int N)
{
  // maxValues[i] : 길이 i인 철근을 팔 때의 최대 이익
  int maxValues[N + 1];

  maxValues[0] = 0;   // 길이 0인 철근의 가격은 0

  // 길이 1에서 N까지 계산해 올라갑니다.
  for(int i = 1; i <= N; i++)
  {
    maxValues[i] = INT_MIN;
    // 길이 i인 철근은 i 길이에 해당되는 가격표(valule[i - 1])까지만 필요합니다.
    for(int j = 1; j <= i; j++)
    {
      // i - j 길이의 최대 이익에 j 길이 철근의 가격을 더하면 i 길이 철근의 
      // 판매 가격을 구할 수 있으며, 모든 j에 대해서 최댓값을 취하면
      // 길이 i인 철근을 판매할 때의 최대 이익을 구할 수 있습니다.
      maxValues[i] = getMax(maxValues[i], 
                            value[j] + maxValues[i - j]);
    }
  }

  for(int i = 0; i <= N; i++)
  {
    printf("%3d", maxValues[i]);
  }
  printf("\n");

  return maxValues[N];
}

int main()
{
  int value[] = {0, 1, 5, 8, 9, 10, 17, 17, 20};
  int N = 8;
  printf("길이 %d인 철근을 잘라서 팔 때 최대 %d의 이익을 얻을 수 있습니다.\n", N, maxValue(value, N));
  return 0;
}