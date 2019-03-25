#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int isInterleaving(char* A, char* B, char* C){
  // A, B, C 세 문자열의 길이를 구합니다.
  int M = strlen(A);
  int N = strlen(B);
  int lengthC = strlen(C);

  // A와 B 문자열의 길이의 합이 C 문자열의 길이와 다를 때
  if(lengthC != M + N)
    return false;

  // 간삽 여부를 저장하는 2차원 배열
  bool ilMatrix[M + 1][N + 1];

  ilMatrix[0][0] = true;  // (0, 0)은 T

  // 첫 번째 열을 채웁니다.
  for(int i = 1; i <= M; i++)
  {
    if(A[i - 1] != C[i - 1])
      ilMatrix[i][0] = false;
    else
      ilMatrix[i][0] = ilMatrix[i - 1][0];
  }

  // 첫 번째 행을 채웁니다.
  for(int j = 1; j <= N; j++)
  {
    if(B[j - 1] != C[j - 1])
      ilMatrix[0][j] = false;
    else
      ilMatrix[0][j] = ilMatrix[0][j - 1];
  }

  // 나머지 셀을 채웁니다.
  for(int i = 1; i <= M; i++){
    for(int j = 1; j <= N; j++){
      // 현재 셀의 A, B, C의 글자
      char currentA = A[i - 1];
      char currentB = B[j - 1];
      char currentC = C[i + j - 1];
      // C의 글자가 A의 글자와 같고 B의 글자와 다를 때
      if(currentA == currentC && currentB != currentC)
        ilMatrix[i][j] = ilMatrix[i - 1][j];
      // C의 글자가 B의 글자와 같고 A의 글자와 다를 때
      else if(currentA != currentC && currentB == currentC)
        ilMatrix[i][j] = ilMatrix[i][j - 1];
      // A, B, C 글자 모두가 같을 때
      else if(currentA == currentC && currentB == currentC)
        ilMatrix[i][j] = ilMatrix[i - 1][j] || ilMatrix[i][j - 1];
      // C의 글자가 A, B 두 글자 어느 쪽과도 다를 때
      else
        ilMatrix[i][j] = false;      
    }
  }

  // 완성된 행렬을 출력합니다.
  for(int i = 0; i <= M; i++){
    for(int j = 0; j <= N; j++){
      printf("%c ", ilMatrix[i][j]? 'T': 'F');
    }
    printf("\n");
  }
  return ilMatrix[M][N];
}

int main()
{
  char a[10] = "bcc";
  char b[10] = "bbca";
  char c[10] = "bbcbcac";

  int check = isInterleaving(a, b, c);
  printf("%s는 %s와 %s의 간삽", c, a, b);
  if(check == true)
    printf("입니다.\n");
  else
    printf("이 아닙니다.\n");
  
  return 0;
}