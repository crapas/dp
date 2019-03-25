#include <stdio.h>

int numOfPaths(int m, int n){
  // 종료 조건
  if(m == 0 && n == 0)  // 방 (0, 0)
    return 0;
  if(m == 0 || n == 0)  // 첫 번째 행 또는 첫 번째 열
    return 1;

  // 재귀 호출
  return numOfPaths(m - 1, n) + numOfPaths(m, n - 1);
}

int main(){
  int M, N;
  printf("방의 구조를 입력하세요 : ");
  scanf("%d %d", &M, &N);
  // 인덱스가 0 부터 이므로 M - 1, N - 1을 파라미터로 호출합니다.
  printf("총 경로의 수는 %d개 입니다.\n", numOfPaths(M - 1, N - 1));
  return 0;
}