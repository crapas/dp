#include <stdio.h>
#include <string.h>
#define M_MAX 30
#define N_MAX 30

// LCSL_Length를 저장할 캐시
int LCSLTable[M_MAX][N_MAX];

// 두 수 중 큰 값을 반환하는 도우미 함수
int getMax(int a, int b)
{
  return a > b? a: b;
}

int lcs_length(char* X, char* Y, int m, int n)
{
  // 종료 조건은 두 문자열 중 하나가 빈 문자열일 때이며,
  // 이때의 LCS_LENGTH는 0입니다.
  if(m == 0 || n == 0)
    return 0;

  // 이미 캐시에 계산된 값이 있다면 (즉 -1이 아니라면)
  // 캐시의 값을 반환합니다.
  if(LCSLTable[m][n] != -1)
    return LCSLTable[m][n];

  // 문자열의 마지막 글자를 비교해 조건에 따라 재귀 호출합니다.
  if(X[m - 1] == Y[n - 1])
    LCSLTable[m][n] = 1 + lcs_length(X, Y, m - 1, n - 1);
  else
    LCSLTable[m][n] = getMax(lcs_length(X, Y, m, n - 1),
                             lcs_length(X, Y, m - 1, n));  
  return LCSLTable[m][n];
}

// 재귀 함수를 처음 호출하기 전 LCSLTable을 초기화해야 합니다.
int initAndLCSLength(char *X, char *Y, int m, int n)
{
  for(int i = 0; i <= m; i++)
    for(int j = 0; j <= m; j++)
      LCSLTable[i][j] = -1;

  return lcs_length(X, Y, m, n);
}

int main()
{
  // 다음 Test Case는 메모 전략을 사용하지 않았을 때 매우 오래 걸리는 Test Case입니다.
  // 메모 전략을 사용함으로써 얼마나 실행 시간이 줄어들었는지를 확인해봅시다.
  //char X[30] = "AAACCGTGAGTTATTCGTTCTAGAA";
  //char Y[30] = "CACCCCTAAGGTACCTTTGGTTC";

  char X[30] = "ABCD";
  char Y[30] = "AEBD";
  printf("[%s]와 [%s]의 LCS_LENGTH의 값은 %d입니다.\n", 
          X, Y, initAndLCSLength(X, Y, strlen(X), strlen(Y)));
  return 0;
}