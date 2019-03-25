#include <stdio.h>
#include <limits.h>
#define MAX_N 10

// 메모를 저장할 배열
int maxValues[MAX_N] = {0};

int getMax(int a, int b)
{
  return a > b? a: b;
}

// value[i]는 길이 i인 철근의 가격입니다.
int maxValue(int *value, int N)
{
  if(N <= 0)
    return 0;
  
  // 이미 계산된 값이 있으면 그 값을 반환
  if(maxValues[N - 1] != 0)
    return maxValues[N - 1];

  maxValues[N - 1] = INT_MIN;

  for(int i = 1; i <= N; i++)
  {
    maxValues[N - 1] = getMax(maxValues[N - 1], 
                   value[i] + maxValue(value, N - i));
  }

  return maxValues[N - 1];
}

int main()
{
  int value[] = {0, 1, 5, 8, 9, 10, 17, 17, 20};
  int N = 8;
  printf("길이 %d인 철근을 잘라서 팔 때 최대 %d의 이익을 얻을 수 있습니다.\n", N, maxValue(value, N));
  return 0;
}