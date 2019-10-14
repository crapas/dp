#include <stdio.h>
#define N 4

// 2차원 배열 형태의 요금표
int cost[4][4] = {{ 0, 10, 75, 94},
                  {-1,  0, 35, 50},
                  {-1, -1,  0, 80},
                  {-1, -1, -1,  0}
                 };

// 출발역(s)에서 도착역(d)까지의 최소 요금을 계산합니다.
int minCost(int s, int d)
{
  if(s == d || s == d - 1)
    return cost[s][d];
  int minValue = cost[s][d];
  // 최솟값을 찾기 위해서 모든 중간 역에 대해서 계산해봅니다.
  for(int i = s + 1; i < d; i++)
  {
    // s번 역에서 i번 역까지의 최소 요금과
    // i번 역에서 d번 역까지의 최소 요금의 합
    int temp = minCost(s, i) + minCost(i, d);
    if(temp < minValue)
      minValue = temp;
  }
  return minValue;
}

int main()
{
  int s = 0;
  int d = 3;
  printf("%d번 역에서 %d번 역까지의 최소 비용은 %d입니다.\n", 
        s, d, minCost(s, d));
  return 0;
}
