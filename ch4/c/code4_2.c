#include <stdio.h>

#define M 3
#define N 4

int getMin(int a, int b)
{
  return a < b? a: b;
}

// 셀 (0, 0)에서 셀(m, n)까지의 최소 이동 비용을 계산합니다.
int minPathCost(int cost[M][N], int m, int n)
{
  if(m == 0 && n == 0)  // 셀 (0, 0)이 목적지인 경우
    return cost[0][0];
  if(m == 0)            // 목적지가 제일 윗 행에 있을 때
    return minPathCost(cost, 0, n - 1) + cost[0][n];
  if(n == 0)            // 목적지가 제일 왼쪽 열에 있을 때
    return minPathCost(cost, m - 1, 0) + cost[m][0];

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