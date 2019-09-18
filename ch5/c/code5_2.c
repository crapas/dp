#include <stdio.h>
#include <string.h>

int getMinimum(int a, int b, int c)
{
  if(a >= c && b >= c)
    return c;
  return a > b? b: a;
}

//#define M 7
//#define N 9
int editDistance(char* str1, char* str2, int m, int n)
{
  int EditD[m + 1][n + 1];

  for(int j = 0; j <= n; j++) // 제일 위 행
    EditD[0][j] = j;

  for(int i = 0; i <= m; i++) // 제일 왼쪽 열
    EditD[i][0] = i;

  for(int i = 1; i <= m; i++)
  {
    for(int j = 1; j <= n; j++)
    {
      // 두 글자가 같다면
      if(str1[i - 1] == str2[j - 1])
        EditD[i][j] = EditD[i - 1][j - 1];
      // 두 글자가 다르다면
      else
        EditD[i][j] = getMinimum(EditD[i][j - 1],
                                 EditD[i - 1][j],
                                 EditD[i - 1][j - 1]) + 1;
      
    }
  }

  // EditD 행렬 출력
  for(int i = 0; i <= m; i++)
  {
    for(int j = 0; j <= n; j++)
    {
      printf("%2d", EditD[i][j]);
    }
    printf("\n");
  }
  return EditD[m][n];
}

int main()
{
  char str1[32], str2[32];
  printf("두 단어를 입력하세요 : ");
  scanf("%s %s", str1, str2);
  printf("두 단어 [%s] [%s] 사이의 최소 교정 비용은 %d입니다.\n", 
    str1, str2, editDistance(str1, str2, strlen(str1), strlen(str2)));
  return 0;    
}
