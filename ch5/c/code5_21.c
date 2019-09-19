#include <stdio.h>
#include <string.h>

int LPS_length(char *str, int n)
{
  // 빈 문자열일 때
  if(str == NULL || *str == '\0')
    return 0;
  
  // table[i][j]는 str[i]에서 str[j]까지의 길이 j - i + 1 문자열의
  // 최장 회문 부분 수열의 길이를 저장합니다.
  int LPSL_table[n][n];

  // 길이가 1인 문자열은 그 자체로 회문이므로 LPSL의 값은 1입니다.
  for(int i = 0; i < n; i++)
    LPSL_table[i][i] = 1;
  
  // 길이가 2인 문자열의 LPSL부터 차례로 채워나갑니다.
  for(int k = 2; k <= n; k++)
  {
    for(int i = 0; i < n - k + 1; i++)
    {
      int j = i + k - 1;
      // 길이가 2이며 두 글자가 모두 같으면 LPSL은 2입니다.
      if(str[i] == str[j] && k == 2)
        LPSL_table[i][j] = 2;
      // 앞뒤 글자가 같으면 두 글자를 제외한 문자열의 
      // LPS에 두 글자를 추가합니다. (LPSL_table[i + 1][j - 1] + 2)
      else if(str[i] == str[j])
        LPSL_table[i][j] = LPSL_table[i + 1][j - 1] + 2;
      // 앞뒤 글자가 다른 경우 LPS가 바뀌지 않으므로 
      // 앞 글자를 제외한 문자열의 LPSL과 뒤 글자를 제외한 문자열의 LPSL 중 
      // 큰 값을 가져오면 됩니다.
      else 
        LPSL_table[i][j] = LPSL_table[i][j - 1] > LPSL_table[i + 1][j]? 
                           LPSL_table[i][j - 1]: LPSL_table[i + 1][j];
    }
  }

  // 완성된 LPSL_table을 출력해봅니다.
  for(int i = 0; i < n; i++)
  {
    for(int j = 0; j < n; j++)
    {
      if(i > j)
        printf("  -");
      else
        printf("%3d", LPSL_table[i][j]);
    }
    printf("\n");
  }

  return LPSL_table[0][n - 1];
}

int main()
{
  char str[] = "BBABCBCAB";
  printf("%s의 최장 회문 부분 수열의 길이는 %d입니다.\n", 
         str, LPS_length(str, strlen(str)));
  return 0;
}