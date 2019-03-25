#include <stdio.h>
#define N 4

// 2차원 배열 형태의 요금표
int cost[4][4] = {{ 0, 10, 75, 94},
                  {-1,  0, 35, 50},
                  {-1, -1,  0, 80},
                  {-1, -1, -1,  0}
                 };

// 메모에 사용할 캐시
int memo[N][N] = {0};

// 출발역(s)에서 도착역(d)까지의 최소 요금을 계산합니다.
int minCost(int s, int d)
{
  if(s == d || s == d - 1)
    return cost[s][d];

  // 값이 계산되지 않은 경우에만 블록 안으로 들어가서 계산합니다.
  if(memo[s][d] == 0)
  {
    // 재귀 호출을 사용하는 코드와 비슷합니다.
    int minValue = cost[s][d];

    for(int i = s + 1; i < d; i++)
    {
      int temp = minCost(s, i) + minCost(i, d);
      if(temp < minValue)
        minValue = temp;
    }

    // 계산된 최소 요금을 캐시에 저장
    memo[s][d] = minValue;
  }
  return memo[s][d];
}


int main()
{
  int s = 0;
  int d = 3;
  printf("%d번 역에서 %d번 역 까지의 최소 비용은 %d입니다.\n", 
        s, d, minCost(s, d));
  return 0;
}
