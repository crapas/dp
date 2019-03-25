#include <stdio.h>

int waysToScore(int n)
{
  if(n < 0) return 0;
  if(n == 0) return 1;
  return waysToScore(n - 10)
         + waysToScore(n - 5)
         + waysToScore(n - 3);
}

int main()
{
  printf("목적 점수를 입력하세요 : ");
  int N;
  scanf("%d", &N);
  printf("%d점 까지의 경우의 수는 %d 입니다.\n", N, waysToScore(N));
  return 0;
}