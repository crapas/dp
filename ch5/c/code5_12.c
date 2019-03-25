#include <stdio.h>
#include <string.h>

// 두 수 중 큰 값을 반환하는 도우미 함수
int getMax(int a, int b)
{
  return a > b? a: b;
}

int lcs_length(char* X, char* Y, int m, int n)
{  
  int LCSTable[m + 1][n + 1];

  // int LCSTable[m + 1][n + 1] = {0}과 같이
  // 배열을 선언할 때 0으로 초기화하면 굳이 첫 열과 첫 행의 값을
  // 0으로 만드는 코드를 추가하지 않아도 됩니다.
  // 여기서는 설명을 위해서 이 과정을 진행합니다.

  // 첫 번째 열을 0으로 채웁니다.
  for(int i = 0; i <= m; i++)
    LCSTable[i][0] = 0;
  
  // 첫 번째 행을 0으로 채웁니다.
  for(int j = 0; j <= n; j++)
    LCSTable[0][j] = 0;

  // 배열의 나머지 셀을 채웁니다.
  for(int i = 1; i <= m; i++){
    for(int j = 1; j <= n; j++){
      if(X[i - 1] == Y[j - 1])
        LCSTable[i][j] = LCSTable[i - 1][j - 1] + 1;
      else
        LCSTable[i][j] = getMax(LCSTable[i - 1][j], LCSTable[i][j - 1]);      
    }
  }

  // LCSTable을 출력해 봅니다.
  for(int i = 0; i <= m; i++){
    for(int j = 0; j <= n; j++){
      printf("%3d", LCSTable[i][j]);
    }
    printf("\n");
  }

  // LCS를 출력합니다.
  int LCSLength = LCSTable[m][n];
  printf("LCS_LENGTH : %d\n", LCSLength);
  char LCS[LCSLength + 1];
  LCS[LCSLength] = '\0';
  LCSLength--;

  int i = m, j = n;
  while(i > 0 && j > 0){
    if(X[i - 1] == Y[j - 1])
    {
      LCS[LCSLength] = X[i - 1];
      i--;
      j--;
      LCSLength--;
    }
    else if(LCSTable[i - 1][j] > LCSTable[i][j - 1])
      i--;
    else 
      j--;
  }
  printf("LCS is %s\n", LCS);

  return LCSTable[m][n];
}

int main()
{
  // 다음 Test Case는 재귀 호출을 사용할 때 매우 오래 걸리는 Test Case입니다.
  // 같은 테스트 케이스로 다른 접근 법으로 구현했을 때의 
  // 실행 시간을 비교 체험해 봅시다.
  char X[30] = "AAACCGTGAGTTATTCGTTCTAGAA";
  char Y[30] = "CACCCCTAAGGTACCTTTGGTTC";
  //char X[30] = "ABCD";
  //char Y[30] = "AEBD";
  printf("[%s]와 [%s]의 LCS_LENGTH의 값은 %d입니다.\n", 
          X, Y, lcs_length(X, Y, strlen(X), strlen(Y)));
  return 0;
}