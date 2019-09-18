#include <stdio.h>

#define M 3
#define N 4

int getMin(int a, int b)
{
  return a < b? a: b;
}

/* 행렬의 왼쪽 위가 (0, 0), 오른쪽 아래가 (m, n) 셀로 0부터 시작하므로
 * 이 MxN 크기의 행렬이 주어졌을 때 m = M - 1, n = N - 1이 됩니다.
 * cost 행렬을 배열로 선언하거나 함수를 호출할 때 주의합시다. */
int minPathCost(int cost[M][N], int m, int n)
{
  int x = minPathCost(cost, m-1, n);
  int y = minPathCost(cost, m, n-1);
  // getMin()은 두 수 중 작은 수를 반환하는 도우미 함수입니다.
  return getMin(x, y) + cost[m][n];
}

int main()
{
  int cost[M][N] = {1, 3, 5, 8, 4, 2, 1, 7, 4, 3, 2, 3};
  printf("최소 이동 비용은 %d입니다.\n", minPathCost(cost, M - 1, N - 1));
  return 0;
}