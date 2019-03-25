#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

// 완전 탐색으로 계산
int maxSubStringLength(char* str)
{
  int n = strlen(str);
  int maxLen = 0;

  // i = 부분 문자열의 시작 인덱스
  for(int i = 0; i < n; i++)
  {
    // j = 부분 문자열의 끝 인덱스 (짝수 길이)
    for(int j = i + 1; j < n; j += 2)
    {
      // len = 현재 부분 문자열의 길이
      int len = j - i + 1;

      // 만약 지금까지의 maxLen이 검사하려는 문자열보다 길면
      // 현재 문자열을 검사(앞쪽과 뒤쪽 절반의 숫자의 합이 같은지)하지 않습니다.
      if(maxLen >= len)
        continue;
      int lSum = 0, rSum = 0;
      for(int k = 0; k < len / 2; k++)
      {
        lSum += (str[i + k] - '0');
        rSum += (str[i + k + len / 2] - '0');
      }
      if(lSum == rSum)
        maxLen = len;
    }
  }
  return maxLen;
}


// 다이나믹 프로그래밍으로 계산
int maxSubStringLength2(char* str){
  int n = strlen(str);
  int maxLen = 0;

  // sum[i][j] = 인덱스 i에서 인덱스 j까지의 숫자의 합
  // i > j인 경우의 값은 사용하지 않습니다.
  int sum[n][n];

  // 행렬의 대각선 아래쪽(i>j)은 사용하지 않습니다.
  // 대각선 위치의 값을 채워 넣습니다.
  for(int i = 0; i < n; i++)
    sum[i][i] = str[i] - '0';

  for(int len = 2; len <= n; len++)
  {
    // 현재 부분 문자열의 i와 j를 선택합니다.
    for(int i = 0; i < n - len + 1; i++)
    {
      int j = i + len - 1;
      int k = len / 2;
      // sum[i][j]의 값을 계산
      sum[i][j] = sum[i][j - k] + sum[j - k + 1][j];
      // len이 짝수이고, 왼쪽과 오른쪽 절반의 합이 같으며
      // len이 maxLen보다 크면 maxLen을 갱신합니다.
      if(len % 2 == 0 && sum[i][j - k] == sum[j - k + 1][j] && len > maxLen)
        maxLen = len;
    }
  }
  return maxLen;
}


int main()
{
  // 난수 시드
  srand(time(NULL));
  printf("생성할 숫자열의 길이를 입력하세요 : ");
  int n;
  scanf("%d", &n);

  // 길이 n의 무작위 난수 숫자열을 만듭니다.
  char numStr[n + 1];
  numStr[n] = '\0';
  numStr[0] = rand() % 9 + '1';
  for(int i = 1; i < n; i++)
    numStr[i] = rand() % 10 + '0';

  printf("생성된 숫자열 : %s\n", numStr);
 
  int result1 = maxSubStringLength(numStr);
  int result2 = maxSubStringLength2(numStr);
  
  printf("[완전 탐색] 결과 : %d\n", result1);
  printf("[다이나믹 프로그래밍] 결과 : %d\n", result2);
  return 0;
}