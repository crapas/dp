// 예제 코드를 일부 수정합니다. 출발 지점과 도착 지점이 같은 경우는 1이기 때문입니다.
// 오류를 사과 드립니다.

#include <stdio.h>

int numOfPaths(int m, int n)
{
  int cache[m][n];

  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      if(i == 0 || j == 0)
        cache[i][j] = 1;
      else
        cache[i][j] = cache[i - 1][j] + cache[i][j - 1];
    }
  }
  return cache[m - 1][n - 1];
}

int main()
{
  int M, N;
  printf("방의 구조를 입력하세요 : ");
  scanf("%d %d", &M, &N);
  
  printf("총 경로의 수는 %d개입니다.\n", numOfPaths(M, N));
  return 0;
}