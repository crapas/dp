#include <stdio.h>

// 2차원 배열 형태의 요금표
int cost[4][4] = {{ 0, 10, 75, 94},
                  {-1,  0, 35, 50},
                  {-1, -1,  0, 80},
                  {-1, -1, -1,  0}
                 };

int minCost(int N)
{
  // minValue[i] = 0번 역에서 i번 역까지의 최소 요금
  int minValue[N + 1];
  minValue[0] = 0;
  // cost[j][i] : j번 역에서 i번 역까지 바로 가는 요금
  minValue[1] = cost[0][1];

  for(int i = 2; i <= N; i++)
  {
    minValue[i] = cost[0][i];
    for(int j = 1; j < i; j++)
      if(minValue[i] > minValue[j] + cost[j][i])
        minValue[i] = minValue[j] + cost[j][i];
  }
  return minValue[N];
}

int main()
{
  int d = 3;
  printf("0번 역에서 %d번 역 까지의 최소 비용은 %d입니다.\n", 
         d, minCost(d));
  return 0;
}
