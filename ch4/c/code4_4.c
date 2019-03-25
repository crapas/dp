#include <stdio.h>

/* 재귀 호출이나 메모 전략을 사용할 때와 마찬가지로
 * 셀 (0, 0)에서 셀 (2, 3) 까지의 최소 이동 비용을 구할 때의
 * M과 N의 값은 3(m + 1)과 4(n + 1)입니다.
 * cost 배열과 MEM 배열을 선언할 때 주의합시다 */
#define M 3
#define N 4

int getMin(int a, int b)
{
  return a < b? a: b;
}

int minPathCost(int cost[M][N])
{
  int MEM[M][N] = {0};
  MEM[0][0] = cost[0][0];

  // 제일 윗쪽 행
  for(int j = 1; j < N; j++)
    MEM[0][j] = MEM[0][j - 1] + cost[0][j];

  // 제일 왼쪽 열
  for(int i = 1; i < M; i++)
    MEM[i][0] = MEM[i - 1][0] + cost[i][0];

  // 나머지 셀을 채워 나갑니다.
  for(int i = 1; i < M; i++)
    for(int j = 1; j < N; j++)
      MEM[i][j] = getMin(MEM[i - 1][j], MEM[i][j - 1]) + cost[i][j];

  // 완성된 배열을 출력해 봅시다.
  for(int i = 0; i < M; i++)
  {
    for(int j = 0; j < N; j++)
      printf("%3d", MEM[i][j]);
    printf("\n");
  }
  return MEM[M-1][N-1];
}

int main()
{
  int cost[M][N] = {1, 3, 5, 8, 4, 2, 1, 7, 4, 3, 2, 3};
  printf("최소 이동 비용은 %d입니다.\n", minPathCost(cost));
  return 0;
}