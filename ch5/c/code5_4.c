#include <stdio.h>

int numOfPaths(int m, int n){
  int cache[m][n];

  for(int i = 1; i < m; i++)  // 첫 번째 열
    cache[i][0] = 1;
  
  for(int j = 1; j < n; j++)  // 첫 번째 행
    cache[0][j] = 1;

  // 나머지 셀을 채웁니다.
  for(int i = 1; i < m; i++)
    for(int j = 1; j < n; j++)
      cache[i][j] = cache[i - 1][j] + cache[i][j - 1];

  return cache[m - 1][n - 1];
}

int main(){
  int M, N;
  printf("방의 구조를 입력하세요 : ");
  scanf("%d %d", &M, &N);
  
  printf("총 경로의 수는 %d개 입니다.\n", numOfPaths(M, N));
  return 0;
}