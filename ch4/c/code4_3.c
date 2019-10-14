#include <stdio.h>

// 변수를 사용해 전역 변수 배열을 선언할 수 없으므로 상수를 선언하여 사용합니다.
#define M 3
#define N 4

// 결과를 저장(메모)할 전역 변수(캐시)
int MEM[M][N] = {0};

int getMin(int a, int b)
{
  return a < b? a: b;
}

int minPathCost(int cost[M][N], int m, int n)
{
  // 만약 셀 (m, n)의 최소 이동 비용이 이미 계산되어 있다면
  // 다시 계산하지 않습니다.
  if(MEM[m][n] != 0)
    return MEM[m][n];

  if(m == 0 && n == 0)
    MEM[m][n] = cost[0][0];
  else if(m == 0)
    MEM[m][n] = minPathCost(cost, m, n - 1) + cost[0][n];
  else if(n == 0)
    MEM[m][n] = minPathCost(cost, m - 1, n) + cost[m][0];
  else{
    int x = minPathCost(cost, m-1, n);
    int y = minPathCost(cost, m, n-1);
    MEM[m][n] = getMin(x, y) + cost[m][n];
  }
  return MEM[m][n];
}

int main()
{
  int cost[M][N] = {1, 3, 5, 8, 4, 2, 1, 7, 4, 3, 2, 3};
  printf("최소 이동 비용은 %d입니다.\n", minPathCost(cost, M - 1, N - 1));
  return 0;
}